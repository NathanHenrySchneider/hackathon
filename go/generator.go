package main

import "math/rand"

const size = 1024

var ruleset = []int{
	0b10110100, // 45
	0b11010100, // 75
	0b10011010, // 89
	0b10100110, // 101
	0b11010110, // 107
	0b10011110, // 121
	0b11100001, // 135
	0b10101001, // 149
	0b10010101, // 169
	0b10000111, // 225
}

// Generator contains all necessary data to generate a new key
type Generator struct {
	Length  int
	Ruleset int
	Current []int
}

// Generate to key
func (g *Generator) Generate() {
	g.GenerateInitialSeed()
	g.Cycle()
}

// GenerateInitialSeed creates the starting seed
func (g *Generator) GenerateInitialSeed() {
	arr := make([]int, g.Length)
	for idx := range arr {
		arr[idx] = rand.Intn(2)
	}

	g.Current = arr
}

// ChangeRuleSet changes the ruleset
func (g *Generator) ChangeRuleSet() {
	g.Ruleset = ruleset[rand.Int()%len(ruleset)]
}

// Analyze dunno
func (g *Generator) Analyze() {
	arr, count := make([]int, g.Length), 0
	neighborhood := (0 << 2) + (g.Current[0] << 1) + g.Current[1]
	for idx := 2; idx <= g.Length; idx, count = idx+1, count+1 {
		arr[count] = (g.Ruleset >> neighborhood) & 1
		neighborhood = g.bitwiseCalc(neighborhood, idx)
	}

	arr[count] = (g.Ruleset >> neighborhood) & 1
	g.Current = arr
}

// GetCurrentKey return the key currently stored in `Current` as ASCII string
func (g *Generator) GetCurrentKey() string {
	if g.Length != len(g.Current) {
		return ""
	}

	asciiArr := make([]byte, g.Length/8)
	for i := 0; i < g.Length; i += 8 {
		char := 0
		for idx, item := range g.Current[i : i+8] {
			char += (item << (7 - idx))
		}

		char = char % 127
		if char <= 32 {
			char += 33
		}

		if char == 92 {
			char++
		}

		asciiArr[i/8] = byte(char)
	}

	return string(asciiArr)
}

// Cycle runs
func (g *Generator) Cycle() {
	for {
		g.ChangeRuleSet()
		g.Analyze()
	}
}

func (g *Generator) bitwiseCalc(neighborhood int, index int) int {
	neighborhood = (neighborhood << 1) & 7
	if index != g.Length {
		neighborhood = neighborhood | g.Current[index]
	}

	return neighborhood
}
