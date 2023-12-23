package main

func AreAlmostEqual(s1 string, s2 string) bool {
	if s1 == s2 {
		return true
	}
	diff := [2]byte{}
	swapped := false
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			if swapped {
				return false
			}
			if diff[0] == 0 {
				diff[0] = s1[i]
				diff[1] = s2[i]
				continue
			}
			if s1[i] != diff[1] || s2[i] != diff[0] {
				return false
			}
			swapped = true
		}
	}
	return swapped
}
