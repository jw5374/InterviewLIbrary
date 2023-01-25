def uniqueMorseRepresentations(words: list[str]) -> int:
    allTrans = set()
    for word in words:
        allTrans.add(convertToMorse(word))
    return len(allTrans)


def convertToMorse(word: str) -> str:
    morseMap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    res = ""
    for ch in word:
        res += morseMap[ord(ch) - 97]
    return res


print(uniqueMorseRepresentations(["a"]))

