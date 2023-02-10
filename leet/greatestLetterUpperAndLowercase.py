def greatestLetter(s: str) -> str:
    letters = {}
    greatest = -1
    for letter in s:
        letters[letter] = True
    for letter in s:
        if letter.lower() in letters and letter.upper() in letters:
            greatest = max(greatest, ord(letter.upper()))
    return chr(greatest) if greatest != -1 else ""


print(greatestLetter("AbCdEfGhIjK"))

