package main

import(
	"fmt"

)
// a map is the result of applying a function to an array?
// a map can aslo be described as taking several things and associating them with another thing

func romanToInt(s string) int {
	type roman_char struct {
		value int
	}
	var I string = roman_char{value: 1}
	var V string = roman_char{value: 5}
	var X string = roman_char{value: 10}
	var L string = roman_char{value: 50}
	roman_char_array := []{I, V, X, L}

	var roman_chars = []rune{'I', 'V', 'X', 'L', 'C', 'D', 'M'}

}
