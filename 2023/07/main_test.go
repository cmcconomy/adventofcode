package main

import (
	"fmt"
	"testing"
)

func testData() string {
	return `32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483`
}

func TestParse(t *testing.T) {
	input := testData()
	o := parse(input)
	var tvi int

	tvi = len(o)
	if tvi != 5 {
		t.Fatalf("Whoops! got %d", tvi)
	}

	if o[0].hand.compare(o[1].hand, true) != -1 {
		t.Fatalf("Whoops! got %d", o[0].hand.compare(o[1].hand, true))
	}

	if o[1].hand.compare(o[2].hand, true) != 1 {
		t.Fatalf("Whoops! got %d", o[1].hand.compare(o[2].hand, true))
	}

	if o[0].hand.compare(o[0].hand, true) != 0 {
		t.Fatalf("Whoops! got %d", o[0].hand.compare(o[0].hand, true))
	}

	fmt.Println(*o[0].hand)

	// ht := handType(o[0].hand)
	// fmt.Println(ht)

}
