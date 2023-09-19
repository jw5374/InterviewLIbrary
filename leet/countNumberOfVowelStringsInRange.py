vowels = {'a', 'e', 'i', 'o', 'u'}


def vowelStrings(self, words: list[str], left: int, right: int) -> int:
    res = 0
    for s in words[left:right+1]:
        if isVowelString(s):
            res += 1
    return res


def isVowelString(word: str) -> bool:
    return word[0] in vowels and word[-1] in vowels
