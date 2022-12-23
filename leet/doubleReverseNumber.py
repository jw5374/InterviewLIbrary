def isSameAfterReversals(num: int) -> bool:
	copy = num
	return num == reverseNum(reverseNum(copy))

def reverseNum(num: int) -> int:
	res = 0
	while num > 0:
		res *= 10
		res += num % 10
		num //= 10
	return res

print(isSameAfterReversals(0))
