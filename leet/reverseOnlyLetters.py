def reverseOnlyLetters(s: str) -> str:
    split = list(s)
    [left, right] = [0, len(s) - 1]
    while left < right:
        while left < right and not split[left].isalpha():
            left += 1
        while right > left and not split[right].isalpha():
            right -= 1
        if left < right:
            split[left], split[right] = split[right], split[left]
            left += 1
            right -= 1
    return "".join(split)
