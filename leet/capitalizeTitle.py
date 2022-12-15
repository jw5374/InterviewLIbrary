def capitalizeTitle(title: str) -> str:
	titled = title.split(" ")
	for i, word in enumerate(titled):
		if len(word) <= 2:
			titled[i] = word.lower()
		else:
			titled[i] = word.title()
	return " ".join(titled)

print(capitalizeTitle("First leTTeR of EACH Word"))
