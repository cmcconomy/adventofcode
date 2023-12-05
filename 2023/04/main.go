package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type Card struct {
	left  []int
	right []int
}

// ------------------------------------------
// Parsing
// ------------------------------------------

func parseCards(input string) []*Card {
	lines := strings.Split(input, "\n")

	var cards []*Card
	for _, line := range lines {
		cards = append(cards, parseCard(line))
	}

	return cards
}

func parseCard(input string) *Card {
	var left, right []int
	left_segment := input[strings.Index(input, ": ")+1 : strings.Index(input, " | ")]
	right_segment := input[strings.Index(input, " | ")+2:]
	for i := 0; i < len(left_segment)/3; i++ {
		val, err := strconv.Atoi(strings.Trim(left_segment[i*3:(i+1)*3], " "))
		check(err)
		left = append(left, val)
	}
	for i := 0; i < len(right_segment)/3; i++ {
		val, err := strconv.Atoi(strings.Trim(right_segment[i*3:(i+1)*3], " "))
		check(err)
		right = append(right, val)
	}

	return &Card{
		left:  left,
		right: right,
	}
}

// ------------------------------------------
// Part 1
// ------------------------------------------

func allCardPoints(cards []*Card) int {
	sum := 0
	for _, card := range cards {
		sum += singleCardPoints(card)
	}
	return sum
}

func singleCardPoints(card *Card) int {
	card_score := 0
	for _, l := range card.left {
		for _, r := range card.right {
			if l == r {
				if card_score == 0 {
					card_score = 1
				} else {
					card_score *= 2
				}
			}
		}
	}
	return card_score
}

// ------------------------------------------
// Part 2
// ------------------------------------------

func singleCardMatches(card *Card) int {
	matches := 0
	for _, l := range card.left {
		for _, r := range card.right {
			if l == r {
				matches++
			}
		}
	}
	return matches
}

func wonCards(cards []*Card) int {
	wonCards := make(map[int]int)
	cardCount := len(cards)
	for i, card := range cards {
		copiesOwned := 1 + wonCards[i]
		matches := singleCardMatches(card)
		for j := 0; j < matches; j++ {
			wonCards[(i+1)+j] = wonCards[(i+1)+j] + copiesOwned
			cardCount += copiesOwned
		}
	}

	return cardCount
}

// ------------------------------------------
// Main
// ------------------------------------------

func main() {
	input_fname := "./input.txt"
	input, err := os.ReadFile(input_fname)
	check(err)

	cards := parseCards(string(input))
	fmt.Printf("Part 1: %d\n", allCardPoints(cards))
	fmt.Printf("Part 2: %d\n", wonCards(cards))
}
