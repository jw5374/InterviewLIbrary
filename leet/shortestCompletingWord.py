import re

def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    matchChar = re.compile(r"[a-z]+")
    charOccs = {}
    currShortest = "aaaaaaaaaaaaaaaaaaaaa"
    for c in licensePlate:
        ignoringcase = c.lower()
        if not matchChar.match(ignoringcase):
            continue
        if ignoringcase in charOccs:
            charOccs[ignoringcase] += 1
        else:
            charOccs[ignoringcase] = 1
    for word in words:
        if matchWord(charOccs, word) and len(word) < len(currShortest):
            currShortest = word
    return currShortest


def matchWord(characters: dict[str, int], word: str) -> bool:
    charsCopy = characters.copy()
    for c in word:
        if c in charsCopy and charsCopy[c] > 0:
            charsCopy[c] -= 1
    for val in charsCopy.values():
        if val != 0:
            return False
    return True

