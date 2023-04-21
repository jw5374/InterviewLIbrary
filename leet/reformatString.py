def reformat(s: str) -> str:
    alphas = []
    nums = []
    for c in s:
        if c.isalpha():
            alphas.append(c)
        else:
            nums.append(c)
    if not (len(nums)-1 <= len(alphas) <= len(nums)+1):
        return ""
    currLen = min(len(alphas), len(nums))
    for i in range(currLen):
        alphas.append(nums.pop())
        alphas.append(alphas.pop(0))
    if len(nums) > 0:
        alphas.append(nums.pop())
    return "".join(alphas)


print(reformat("ab084b1c2"))

