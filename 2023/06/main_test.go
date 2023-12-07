package main

import (
	"fmt"
	"testing"
)

func testData() string {
	return `Time:      7  15   30
Distance:  9  40  200`
}

func TestParse(t *testing.T) {
	input := testData()
	o := parse(input, false)
	var tvi int

	tvi = len(o.time)
	if tvi != 3 {
		t.Fatalf("Whoops! got %d", tvi)
	}

	d := distances(o, 0)
	if d[3] != 12 {
		t.Fatalf("Whoops! got %d", d[3])
	}

	wc := winCount(o, 0)
	if wc != 4 {
		t.Fatalf("Whoops! got %d", wc)
	}

	em := errorMargin(o)
	if em != 288 {
		t.Fatalf("Whoops! got %d", em)
	}

	o2 := parse(input, true)
	fmt.Println(o2)

	em2 := errorMargin(o2)
	if em != 71503 {
		t.Fatalf("Whoops! got %d", em2)
	}

}
