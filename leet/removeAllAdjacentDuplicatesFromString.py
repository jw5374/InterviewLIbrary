def removeDuplicates(s: str) -> str:
    charArray = list(s)
    charStack = [0]
    i = 1
    while i < len(charArray):
        if len(charStack) > 0 and charArray[i] == charArray[charStack[-1]]:
            while i < len(charArray) and len(charStack) > 0 and charArray[i] == charArray[charStack[-1]]:
                charArray[charStack.pop()] = ""
                charArray[i] = ""
                i += 1
        else:
            charStack.append(i)
            i += 1
    return "".join(charArray)
