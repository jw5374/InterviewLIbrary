def canBeTypedWords(text: str, brokenLetters: str) -> int:
    invalidLetters = {}
    res = 0
    i = 0
    for letter in brokenLetters:
        invalidLetters[letter] = True
    while i < len(text):
        if text[i] in invalidLetters:
            res += 1
            while i < len(text) and text[i] != " ":
                i += 1
        i += 1
    return len(text.split(" ")) - res


print(canBeTypedWords("hello world", "ad"))

