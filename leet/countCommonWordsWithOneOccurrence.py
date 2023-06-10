def countWords(words1: list[str], words2: list[str]) -> int:
    wordsHash = {}
    for word in words1:
        if word in wordsHash:
            wordsHash[word] = -1
        else:
            wordsHash[word] = 1
    for word in words2:
        if word in wordsHash:
            wordsHash[word] -= 1
    return len([count for count in wordsHash.values() if count == 0])
