def prefixCount(words: list[str], pref: str) -> int:
	res = 0
	for word in words:
		if len(pref) > len(word):
			continue
		if word[0:len(pref)] == pref:
			res += 1
	return res

print(prefixCount(["pay","attention","practice","attend"], "at"))
