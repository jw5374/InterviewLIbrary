def stringMatching(words: list[str]) -> list[str]:
    words.sort(key=len)
    res = []
    for i, word in enumerate(words):
        for j in range(len(words) - 1, i, -1):
            if word in words[j]:
                res.append(word)
                break
    return res
