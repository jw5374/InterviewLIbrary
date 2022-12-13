def wordPattern(pattern: str, s: str) -> bool:
	words = s.split(" ")
	hash = {}
	if len(pattern) != len(words):
		return False
	for i, val in enumerate(pattern):
		val += "_"
		if val not in hash and words[i] not in hash:
			hash[val] = words[i]
			hash[words[i]] = val
		elif hash.get(val) != words[i] or hash.get(words[i]) != val:
			return False
	return True

print(wordPattern("abc", "b c a"))
