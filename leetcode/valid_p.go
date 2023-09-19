package main

// i can create a temporary variable that gets appending with any unclosed brackrts and when they are closed they will be removed

func main() {
	isValid("{}")

}

index out of range


func isValid(s string) bool {
	// unclosed brackets holder

	u := []rune{}
	// last index in the entry string
	z := len(u) - 1

	for _, x := range s {
		if string(x) == "(" {
			u = append(u, x)
		} else if string(x) == "[" {
			u = append(u, x)
		} else if string(x) == "{" {
			u = append(u, x)

		} else if string(x) == ")" {
			if string(u[z]) == "(" {
				u = u[:z]
			}
		} else if string(x) == "]" {
			if string(u[z]) == "[" {
				u = u[:z]
			}
		} else if string(x) == "}" {
			if string(u[z]) == "{" {
				u = u[:z]
			}
		}

	}

	if len(u) > 0 {
		return false
	} else {
		return true
	}
}
