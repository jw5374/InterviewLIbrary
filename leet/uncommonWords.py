def freqMap(words: list[str]) -> dict[str, int]:
	map = {}
	for word in words:
		if word in map:
			map[word] += 1
		else:
			map[word] = 1
	return map

# initial naive
def uncommonFromSentences(s1: str, s2: str) -> list[str]:
	words1 = s1.split(" ")
	words2 = s2.split(" ")
	hash1 = freqMap(words1)
	hash2 = freqMap(words2)
	res = []
	for key, val in hash2.items():
		if key not in hash1 and val == 1:
			res.append(key)
	for key, val in hash1.items():
		if key not in hash2 and val == 1:
			res.append(key)
	return res

# combining for O(m+n)
def uncommonOnePass(s1: str, s2: str) -> list[str]:
	combined = s1 + " " + s2
	frequency = freqMap(combined.split(" "))
	return [word for word, num in frequency.items() if num == 1]

print(uncommonOnePass("this apple is sweet", "this apple is sour"))
