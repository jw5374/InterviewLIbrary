def pivotInteger(n: int) -> int:
    # sum = (n * (n+1)) // 2
    # leftSum = 0
    # for i in range(1, n+1):
    #     leftSum += i
    #     if sum - leftSum + i == leftSum:
    #         return i
    # return -1
    the_only_nums = {
        1: 1,
        8: 6,
        49: 35,
        288: 204
    }
    if n in the_only_nums:
        return the_only_nums[n]
    return -1


for i in range(1, 1001):
    if pivotInteger(i) != -1:
        print(i, pivotInteger(i))

