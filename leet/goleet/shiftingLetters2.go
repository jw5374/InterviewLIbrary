package main

func ShiftingLetters(s string, shifts [][]int) string {
	chars := []byte(s)
	for _, shift := range shifts {
		chars = shiftInterval(chars, shift)
	}
	return string(chars)
}

func shiftInterval(c []byte, interval []int) []byte {
	direction := interval[2]
	if direction == 0 {
		direction--
	}
	for i := interval[0]; i <= interval[1]; i++ {
		c[i] += byte(direction)
		if c[i] < 97 {
			c[i] = 122
			continue
		}
		if c[i] > 122 {
			c[i] = 97
		}
	}
	return c
}
