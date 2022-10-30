def isValid(s: str) -> bool:
    if(len(s) % 2 != 0):
        return False
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stringArr = list(s)
    i = 0
    sLen = len(stringArr)
    while(i < sLen):
        if(stringArr[i] in brackets.keys()):
            i += 1
        else:
            if(i > 0 and stringArr[i] == brackets[stringArr[i-1]]):
                stringArr.pop(i)
                stringArr.pop(i-1)
                i -= 1
                sLen = len(stringArr)
            else:
                return False
    if(sLen > 0):
        return False
    return True
    
print(isValid("(()])"))    
