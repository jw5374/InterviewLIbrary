def nextGreatestLetter(letters: list[str], target: str) -> str:
    targetVal = ord(target)
    for letter in letters:
        if ord(letter) > targetVal:
            return letter
    return letters[0]
