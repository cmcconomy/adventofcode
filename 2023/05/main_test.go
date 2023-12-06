package main

import (
	"fmt"
	"slices"
	"testing"
)

func testData() string {
	return `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4`
}

func TestParse(t *testing.T) {
	input := testData()
	o := parse(input)
	var tvi int

	tvi = len(o.seeds)
	if tvi != 4 {
		t.Fatalf("Whoops! got %d", tvi)
	}

	fmt.Println(*o.index["seed"])
	tvi = len(o.index["seed"].mappings)
	if tvi != 2 {
		t.Fatalf("Whoops! got %d", tvi)
	}
	fmt.Println(o)

	locs := getLocations(o, false)
	v1 := locs[0]
	if v1 != 82 {
		t.Fatalf("Whoops! got %d", v1)
	}

	m := slices.Min(locs)
	if m != 35 {
		t.Fatalf("Whoops! got %d", m)
	}

	locs2 := getLocations(o, true)
	m2 := slices.Min(locs2)
	if m2 != 46 {
		t.Fatalf("Whoops! got %d", m2)
	}

}
