def mostWordsFound(sentences: list[str]) -> int:
    max = 0
    for sentence in sentences:
        words = countWords(sentence)
        if max < words:
            max = words
    return max


def countWords(sentence: str) -> int:
    res = 0
    for c in sentence:
        if c == " ":
            res += 1
    return res + 1
