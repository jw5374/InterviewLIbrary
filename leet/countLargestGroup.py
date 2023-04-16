def countLargestGroup(n: int) -> int:
    digitSums = {}
    largest = 0
    maxSize = 0
    for num in range(1, n+1):
        sum = digitSum(num)
        if sum in digitSums:
            digitSums[sum].append(num)
        else:
            digitSums[sum] = [num]
    for val in digitSums.values():
        if len(val) > maxSize:
            maxSize = len(val)
            largest = 1
        elif len(val) == maxSize:
            largest += 1
    return largest


def digitSum(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
