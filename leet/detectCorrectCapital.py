def detectCapitalUse(word: str) -> bool:
	if len(word) == 1:
		return True
	flag = word[0].isupper()
	if flag:
		remaining = word[1:]
		return remaining.isupper() or remaining.islower()
	return word.islower()

print(detectCapitalUse("USA"))
