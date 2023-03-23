def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split(" ")
    for i, word in enumerate(words):
        if searchWord == word[0:len(searchWord)]:
            return i + 1
    return -1


print(isPrefixOfWord("i love eating burgers", "burg"))

