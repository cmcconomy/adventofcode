package main

import (
	"fmt"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type Hand struct {
	raw      []int
	handType int
	ordered  []int
}

type Round struct {
	hand *Hand
	bid  int
}

// ------------------------------------------
// Parsing
// ------------------------------------------

func cardVal(char byte) int {
	if char == 'A' {
		return 14
	} else if char == 'K' {
		return 13
	} else if char == 'Q' {
		return 12
	} else if char == 'J' {
		return 11
	} else if char == 'T' {
		return 10
	} else {
		return int(char) - 48
	}
}

const (
	HIGH_CARD       = iota
	ONE_PAIR        = iota
	TWO_PAIR        = iota
	THREE_OF_A_KIND = iota
	FULL_HOUSE      = iota
	FOUR_OF_A_KIND  = iota
	FIVE_OF_A_KIND  = iota
)

func toHand(hand []int) *Hand {
	sortedHand := make([]int, len(hand))
	copy(sortedHand, hand)
	slices.Sort(sortedHand)
	slices.Reverse(sortedHand)

	if sortedHand[0] == sortedHand[1] &&
		sortedHand[1] == sortedHand[2] &&
		sortedHand[2] == sortedHand[3] &&
		sortedHand[3] == sortedHand[4] {
		return &Hand{
			raw:      hand,
			handType: FIVE_OF_A_KIND,
			ordered:  sortedHand,
		}
	} else if sortedHand[0] == sortedHand[1] &&
		sortedHand[1] == sortedHand[2] &&
		sortedHand[2] == sortedHand[3] {
		return &Hand{
			raw:      hand,
			handType: FOUR_OF_A_KIND,
			ordered:  sortedHand,
		}
	} else if sortedHand[1] == sortedHand[2] &&
		sortedHand[2] == sortedHand[3] &&
		sortedHand[3] == sortedHand[4] {
		sortedHand[0], sortedHand[5] = sortedHand[5], sortedHand[0]
		return &Hand{
			raw:      hand,
			handType: FOUR_OF_A_KIND,
			ordered:  sortedHand,
		}
	} else if sortedHand[0] == sortedHand[1] &&
		sortedHand[1] == sortedHand[2] &&
		sortedHand[3] == sortedHand[4] {
		return &Hand{
			raw:      hand,
			handType: FULL_HOUSE,
			ordered:  sortedHand,
		}
	} else if sortedHand[0] == sortedHand[1] &&
		sortedHand[2] == sortedHand[3] &&
		sortedHand[3] == sortedHand[4] {
		sortedHand[0], sortedHand[1], sortedHand[3], sortedHand[4] = sortedHand[3], sortedHand[4], sortedHand[0], sortedHand[1]
		return &Hand{
			raw:      hand,
			handType: FULL_HOUSE,
			ordered:  sortedHand,
		}
	} else if sortedHand[0] == sortedHand[1] &&
		sortedHand[1] == sortedHand[2] {
		return &Hand{
			raw:      hand,
			handType: THREE_OF_A_KIND,
			ordered:  sortedHand,
		}
	} else if sortedHand[1] == sortedHand[2] &&
		sortedHand[2] == sortedHand[3] {
		sortedHand[0], sortedHand[3] = sortedHand[3], sortedHand[0]
		return &Hand{
			raw:      hand,
			handType: THREE_OF_A_KIND,
			ordered:  sortedHand,
		}
	} else if sortedHand[2] == sortedHand[3] &&
		sortedHand[3] == sortedHand[4] {
		sortedHand[0], sortedHand[1], sortedHand[3], sortedHand[4] = sortedHand[3], sortedHand[4], sortedHand[0], sortedHand[1]
		return &Hand{
			raw:      hand,
			handType: THREE_OF_A_KIND,
			ordered:  sortedHand,
		}
	} else if sortedHand[0] == sortedHand[1] &&
		sortedHand[2] == sortedHand[3] {
		return &Hand{
			raw:      hand,
			handType: TWO_PAIR,
			ordered:  sortedHand,
		}
	} else if sortedHand[0] == sortedHand[1] &&
		sortedHand[3] == sortedHand[4] {
		sortedHand[2], sortedHand[4] = sortedHand[4], sortedHand[2]
		return &Hand{
			raw:      hand,
			handType: TWO_PAIR,
			ordered:  sortedHand,
		}
	} else if sortedHand[1] == sortedHand[2] &&
		sortedHand[3] == sortedHand[4] {
		sortedHand[0], sortedHand[1], sortedHand[2], sortedHand[3], sortedHand[4] = sortedHand[1], sortedHand[2], sortedHand[3], sortedHand[4], sortedHand[0]
		return &Hand{
			raw:      hand,
			handType: TWO_PAIR,
			ordered:  sortedHand,
		}
	} else if sortedHand[0] == sortedHand[1] {
		return &Hand{
			raw:      hand,
			handType: ONE_PAIR,
			ordered:  sortedHand,
		}
	} else if sortedHand[1] == sortedHand[2] {
		sortedHand[0], sortedHand[2] = sortedHand[2], sortedHand[0]
		return &Hand{
			raw:      hand,
			handType: ONE_PAIR,
			ordered:  sortedHand,
		}
	} else if sortedHand[2] == sortedHand[3] {
		sortedHand[0], sortedHand[1], sortedHand[2], sortedHand[3] = sortedHand[2], sortedHand[3], sortedHand[0], sortedHand[1]
		return &Hand{
			raw:      hand,
			handType: ONE_PAIR,
			ordered:  sortedHand,
		}
	} else if sortedHand[3] == sortedHand[4] {
		sortedHand[0], sortedHand[1], sortedHand[3], sortedHand[4] = sortedHand[3], sortedHand[4], sortedHand[0], sortedHand[1]
		return &Hand{
			raw:      hand,
			handType: ONE_PAIR,
			ordered:  sortedHand,
		}
	} else {
		return &Hand{
			raw:      hand,
			handType: HIGH_CARD,
			ordered:  sortedHand,
		}
	}
}

func parse(input string) []*Round {
	lines := strings.Split(input, "\n")

	re, err := regexp.Compile(`\s+`)
	check(err)

	var rounds []*Round
	for _, line := range lines {
		parts := re.Split(line, -1)
		hand := []int{}
		for _, cardByte := range []byte(parts[0]) {
			hand = append(hand, cardVal(cardByte))
		}

		val, err := strconv.Atoi(parts[1])
		check(err)
		rounds = append(rounds, &Round{
			hand: toHand(hand),
			bid:  val,
		})
	}

	return rounds
}

// ------------------------------------------
// Part 1
// ------------------------------------------

func (hand1 *Hand) compare(hand2 *Hand, naiveOrder bool) int {
	fmt.Println("Comparing", *hand1, *hand2)
	if hand1.handType < hand2.handType {
		return -1
	} else if hand1.handType > hand2.handType {
		return 1
	} else {
		var hand1Arr, hand2Arr []int
		if naiveOrder {
			hand1Arr = hand1.raw
			hand2Arr = hand2.raw
		} else {
			hand1Arr = hand1.ordered
			hand2Arr = hand2.ordered
		}
		for i := 0; i < 5; i++ {
			if hand1Arr[i] < hand2Arr[i] {
				return -1
			} else if hand1Arr[i] > hand2Arr[i] {
				return 1
			}
		}
	}
	return 0 // equal
}

// ------------------------------------------
// Part 2
// ------------------------------------------

// ------------------------------------------
// Main
// ------------------------------------------

func main() {
	// input_fname := "./input.txt"
	// input, err := os.ReadFile(input_fname)
	// check(err)

	// doc := parse(string(input), false)
	// fmt.Printf("Part 1: %d\n", errorMargin(doc))
	// doc = parse(string(input), true)
	// fmt.Printf("Part 2: %d\n", errorMargin(doc))
}
