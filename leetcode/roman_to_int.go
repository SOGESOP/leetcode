package main

import (
	"fmt"
)

func main() {
	var test_string string = "IV"

	romanToInt(test_string)

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

	var rune_form []rune = []rune(s)
	var int_form []int

	// converts the roman numerals into a integer form, done using runes instead of normal python way to try out runes
	for _, x := range rune_form {
		int_form = append(int_form, roman_char[x])
	}

	var current int
	for i, j := 0, 1; i < len(int_form); i, j = i+1, j+1 {
		current += int_form[i]
		if int_form[i] < int_form[j] {
			current *= -1
		} else if int_form[i] == int_form[j] {

		}

	}

	fmt.Printf("%v", int_form)
	var int_version int

	return int_version
}
