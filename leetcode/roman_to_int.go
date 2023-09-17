package main

import (
	"fmt"
)

func main() {
	var test_string string = "IX"
	test_value := romanToInt(test_string)
	fmt.Printf("%v", test_value)

}

// a map is the result of applying a function to an array?
// a map can aslo be described as taking several things and associating them with another thing

func romanToInt(s string) int {
	// a map that is used to store the dictionary
	roman_char := map[rune]int{
		'I': 1, 'V': 5,
		'X': 10, 'L': 50,
		'C': 100, 'D': 500,
		'M': 1000}
	var rune_form = []rune(s)
	var int_form []int
	// converts the roman numerals into a integer form, done using runes instead of normal python way to try out runes, was unnnecesary as you can just index st ring like python
	for _, x := range rune_form {
		int_form = append(int_form, roman_char[x])
	}

	var current int
	var positive int
	var negative int
	for i := 0; i < len(int_form)-1; i++ {
		j := i + 1
		if int_form[i] == int_form[j] {
			current += int_form[i]
		} else if int_form[i] < int_form[j] {
			current += int_form[i]
			negative += current
			current = 0
		} else if int_form[i] > int_form[j] {
			current += int_form[i]
			positive += current
			current = 0
		}
	}
	// last number is always positive and not considered in the for loop, and then add in any values left in current from last loop
	positive += int_form[len(int_form)-1] + current

	return positive - negative
}
