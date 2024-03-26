package main

import (
	"fmt"
)

func longestCommonPrefix(strs []string) string {

	// dont work on leetcode
	// if slices.Contains(strs, "") {
	// 	return ""
	// }

	// checks for empty string
	for _, s := range strs {
		if s == "" {
			return ""
		}
	}

	// finds the longest word in the list, and then uses that as the reference point
	var inital_prefix string
	for _, x := range strs {
		if len(x) > len(inital_prefix) {
			inital_prefix = x
		}
	}

	// this will store all the prefixes that are created
	prefix_list := []string{}
	// checks each word in the list against the longest
	for _, word := range strs {
		var longest_prefix string
		for idx, x := range word {
			if x != rune(inital_prefix[idx]) {
				break
			} else {
				longest_prefix += string(x)
			}
		}
		prefix_list = append(prefix_list, longest_prefix)
	}
	fmt.Printf("%v", prefix_list)
	// starts from longest possible prefix and keeps going until the shortest one is reached, and finds the shortest one
	for _, x := range prefix_list {
		if len(x) < len(inital_prefix) {
			inital_prefix = x
		}
	}

	return inital_prefix
}
