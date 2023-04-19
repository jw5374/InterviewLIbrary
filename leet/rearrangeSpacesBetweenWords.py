def reorderSpaces(text: str) -> str:
    words = [x for x in text.split(" ") if x != ""]
    numSpaces = 0
    for c in text:
        if c == " ":
            numSpaces += 1
    if len(words) == 1:
        return words[0] + (" " * numSpaces)
    return (" " * (numSpaces // (len(words) - 1))).join(words) + (" " * (numSpaces % (len(words) - 1)))


print(reorderSpaces(" practice   makes   perfect"))

