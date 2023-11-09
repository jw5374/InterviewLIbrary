package main

func AreOccurrencesEqual(s string) bool {
	occs := [26]int{}
	equality := 0
	for _, c := range s {
		occs[c - 97]++
	}
	for _, occ := range occs {
		if occ == 0 {
			continue
		}
		if equality == 0 {
			equality = occ
			continue
		}
		if occ != equality {
			return false
		}
	}
	return true
}
