package main

func Interpret(command string) string {
	res := ""
	i := 0
	for i < len(command) {
		switch string(command[i]) {
		case "G":
			res += "G"
			i++
		case "(":
			if string(command[i+1]) != ")" {
				res += "al"
				i += 4
				break
			}
			res += "o"
			i += 2
		}
	}
	return res
}
