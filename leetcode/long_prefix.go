package main

func longestCommonPrefix(strs []string) string {
	// maks the current string

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
				return longest_prefix
			} else {
				longest_prefix += string(x)
			}
			prefix_list = append(prefix_list, string(x))
		}
	}
	inital_prefix = ""
	for _, x := range prefix_list {
		if len(x) > len(inital_prefix) {
			inital_prefix = x
		}
	}

	return inital_prefix

}
