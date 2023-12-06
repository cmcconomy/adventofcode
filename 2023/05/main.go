package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type RangeMapEntry struct {
	destStart int
	srcStart  int
	rangeLen  int
}

type RangeMap struct {
	srcType  string
	destType string
	mappings []*RangeMapEntry
}

type Almanac struct {
	seeds []int
	index map[string]*RangeMap // lookup convenience
}

// ------------------------------------------
// Parsing
// ------------------------------------------

func parse(input string) *Almanac {
	lines := strings.Split(input, "\n")

	index := make(map[string]*RangeMap)
	var currType string

	seeds := []int{}
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		if line[0:6] == "seeds:" {
			for _, s := range strings.Split(line[7:], " ") {
				num, err := strconv.Atoi(s)
				check(err)
				seeds = append(seeds, num)
			}
		} else {
			tokens := strings.Split(line, " ")
			if len(tokens) == 2 {
				names := strings.Split(tokens[0], "-")
				// init rangeMap
				mappings := []*RangeMapEntry{}
				rangeMap := RangeMap{
					srcType:  names[0],
					destType: names[2],
					mappings: mappings,
				}
				currType = rangeMap.srcType
				index[currType] = &rangeMap
			} else {
				mapEntryValues := []int{}
				for _, s := range strings.Split(line, " ") {
					num, err := strconv.Atoi(s)
					check(err)
					mapEntryValues = append(mapEntryValues, num)
				}
				mapEntry := RangeMapEntry{
					destStart: mapEntryValues[0],
					srcStart:  mapEntryValues[1],
					rangeLen:  mapEntryValues[2],
				}
				index[currType].mappings = append(index[currType].mappings, &mapEntry)
			}
		}
	}

	return &Almanac{
		seeds: seeds,
		index: index,
	}
}

// ------------------------------------------
// Part 1
// ------------------------------------------

func getLocations(almanac *Almanac, seedsAsRange bool) []int {
	// this logic isn't right.. yet.. start from scratch please!
	locations := []int{}
	var seeds []int
	var itemMap *RangeMap

	if seedsAsRange {
		seeds = []int{}
		for i := 0; i < len(almanac.seeds)/2; i++ {
			fmt.Println("  ..v:", almanac.seeds[i*2], "len:", almanac.seeds[2*i+1])
			for j := 0; j < almanac.seeds[2*i+1]; j++ {
				seeds = append(seeds, almanac.seeds[i*2]+j)
			}
		}
	} else {
		seeds = almanac.seeds
	}
	fmt.Println("Using seeds", seeds)

	for _, seed := range seeds {
		itemType := "seed"
		val := seed
		for {
			itemMap = almanac.index[itemType]
			for _, rangeMap := range itemMap.mappings {
				// map val IF the source value is in a map range..
				if val >= rangeMap.srcStart && val < rangeMap.srcStart+rangeMap.rangeLen {
					delta := val - rangeMap.srcStart
					val = rangeMap.destStart + delta
					break
				} // else val stays the same
			}
			itemType = itemMap.destType
			if itemType == "location" {
				locations = append(locations, val)
				break
			}
		}
	}
	return locations
}

// ------------------------------------------
// Part 2
// ------------------------------------------

// ------------------------------------------
// Main
// ------------------------------------------

func main() {
	input_fname := "./input.txt"
	input, err := os.ReadFile(input_fname)
	check(err)

	almanac := parse(string(input))
	fmt.Printf("Part 1: %d\n", slices.Min(getLocations(almanac, false)))
	// fmt.Printf("Part 2: %d\n", slices.Min(getLocations(almanac, true)))
}
