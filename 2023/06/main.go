package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type RaceDoc struct {
	time []int
	dist []int
}

// ------------------------------------------
// Parsing
// ------------------------------------------

func parse(input string, fixKerning bool) *RaceDoc {
	lines := strings.Split(input, "\n")
	var times, dists []int

	re, err := regexp.Compile(`\s+`)
	check(err)

	if fixKerning {
		parts := strings.Split(lines[0], ":")
		lines[0] = parts[0] + ": " + re.ReplaceAllString(parts[1], "")
		parts = strings.Split(lines[1], ":")
		lines[1] = parts[0] + ": " + re.ReplaceAllString(parts[1], "")
	}

	for _, str := range re.Split(lines[0], -1)[1:] {
		val, err := strconv.Atoi(str)
		check(err)
		times = append(times, val)
	}
	for _, str := range re.Split(lines[1], -1)[1:] {
		val, err := strconv.Atoi(str)
		check(err)
		dists = append(dists, val)
	}

	return &RaceDoc{
		time: times,
		dist: dists,
	}
}

// ------------------------------------------
// Part 1
// ------------------------------------------

func distances(doc *RaceDoc, index int) []int {
	var d []int
	for secondsHeld := 0; secondsHeld <= doc.time[index]; secondsHeld++ {
		secondsMoving := doc.time[index] - secondsHeld
		speed := secondsHeld
		distance := secondsMoving * speed
		d = append(d, distance)
	}
	return d
}

func winCount(doc *RaceDoc, index int) int {
	count := 0
	for _, dist := range distances(doc, index) {
		if dist > doc.dist[index] {
			count++
		}
	}
	return count
}

func errorMargin(doc *RaceDoc) int {
	margin := 1
	for i := 0; i < len(doc.time); i++ {
		margin *= winCount(doc, i)
	}
	return margin
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

	doc := parse(string(input), false)
	fmt.Printf("Part 1: %d\n", errorMargin(doc))
	doc = parse(string(input), true)
	fmt.Printf("Part 2: %d\n", errorMargin(doc))
}
