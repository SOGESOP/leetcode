package main

import (
	"strconv"
)

func isPalindrome(x int) bool {
	var temp string = strconv.Itoa(x)
	// this will reverse the string by going through each character as a rune and then changing the order of the list of runes (the rune form of the string)
	var byte_str = []rune(temp)
	for i, j := 0, len(byte_str)-1; i < j; i, j = i+1, j-1 {
		byte_str[i], byte_str[j] = byte_str[j], byte_str[i]
	}
	var reversed = string(byte_str)
	if temp == reversed {
		return true
	} else {
		return false
	}

}
