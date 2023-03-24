vowels = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True
    }


def reverseVowels(s: str) -> str:
    chars = list(s)
    [i, j] = [0, len(chars)-1]
    while True:
        while i < j and chars[i].lower() not in vowels:
            i += 1
        while j > i and chars[j].lower() not in vowels:
            j -= 1
        if i == j:
            break
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1
    return "".join(chars)


print(reverseVowels("leetcode"))

