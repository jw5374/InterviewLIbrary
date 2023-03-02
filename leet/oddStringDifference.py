def oddString(words: list[str]) -> str:
    hash = {}
    for word in words:
        diffStr = findDiff(word)
        if diffStr in hash:
            hash[diffStr][0] += 1
        else:
            hash[diffStr] = [1, word]
    for key, val in hash.items():
        if val[0] == 1:
            return val[1]


def findDiff(word: str) -> str:
    res = 0
    for i in range(len(word)-1):
        res += ord(word[i+1]) - ord(word[i])
        res *= 10
    return str(res)


print(oddString(["aaa","bob","ccc","ddd"]))

