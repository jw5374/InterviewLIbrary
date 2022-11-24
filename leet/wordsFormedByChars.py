def countCharacters(words: list[str], chars: str) -> int:
	hash = {}
	res = 0
	for i in range(len(chars)):
		if(chars[i] in hash):
			hash[chars[i]] += 1
		else:
			hash[chars[i]] = 1
	for word in words:
		if(checkFreq(word, hash)):
			res += len(word)
	return res

def checkFreq(word: str, freq: dict):
	hashCopy = freq.copy()
	for i in range(len(word)):
		if(word[i] not in hashCopy):
			return False
		if(hashCopy[word[i]] == 0):
			return False
		hashCopy[word[i]] -= 1
	return True

print(countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
