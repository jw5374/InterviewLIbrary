def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    return convertWord(firstWord) + convertWord(secondWord) == convertWord(targetWord)


def convertWord(word: str) -> int:
    res = list(word)
    for i in range(len(res)):
        res[i] = str(ord(res[i]) - 97)
    return int("".join(res))


print(isSumEqual("acb", "cba", "cdb"))

