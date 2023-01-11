def reversePrefix(word: str, ch: str) -> str:
    try:
        wordSplit = list(word)
        [start, end] = [0, wordSplit.index(ch)]
        while start < end:
            wordSplit[start], wordSplit[end] = wordSplit[end], wordSplit[start]
            start += 1
            end -= 1
        return "".join(wordSplit)
    except ValueError:
        return word


print(reversePrefix("abcdefd", "d"))

