def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return True
    [left, right] = [1, num]
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 == num:
            return True
        if mid ** 2 < num:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(isPerfectSquare(14))

