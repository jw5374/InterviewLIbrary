keyRows = [set(list("qwertyuiop")), set(list("asdfghjkl")), set(list("zxcvbnm"))]


def findWords(self, words: list[str]) -> list[str]:
    res = []
    for word in words:
        curword = word.lower()
        curRow = 0
        for i in range(0, 3):
            if curword[0] in keyRows[i]:
                curRow = i
                break
        for c in curword:
            if c not in keyRows[curRow]:
                break
        else:
            res.append(word)
    return res
