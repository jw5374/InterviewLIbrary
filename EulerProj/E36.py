maxnum = 1000000


def isPalindrome(val: str) -> bool:
    [left, right] = [0, len(val) - 1]
    while left < right:
        if val[left] != val[right]:
            return False
        left += 1
        right -= 1
    return True


# naively casting values
def doubleBasePalindromesSum() -> int:
    res = 0
    for i in range(1, maxnum + 1):
        decimalNum = str(i)
        binaryNum = bin(i).split("b")[-1]
        if isPalindrome(decimalNum) and isPalindrome(binaryNum):
            print(i)
            res += i
    return res


print(doubleBasePalindromesSum())
