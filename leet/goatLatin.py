def toGoatLatin(sentence: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    words = sentence.split(" ")
    for i, word in enumerate(words):
        newword = word
        if word[0].lower() in vowels:
            newword += "ma"
        else:
            newword = word[1:] + word[0] + "ma"
        newword += "a" * (i + 1)
        words[i] = newword
    return " ".join(words)
