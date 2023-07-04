import re


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    normalized = re.sub("[!?',;.]", " ", paragraph).lower().split(" ")
    wordOccs = {}
    banned = set(banned)
    res = [0, ""]
    for word in normalized:
        if not word:
            continue
        if word in wordOccs:
            wordOccs[word] += 1
        else:
            wordOccs[word] = 1
        if word not in banned and res[0] < wordOccs[word]:
            res = [wordOccs[word], word]
    return res[1]
