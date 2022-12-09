def isHappy(n: int) -> bool:
	history = set()
	num = n
	while num > 1:
		history.add(num)
		num = sumSquaredDigits(num)
		if num in history:
			return False
	return True

def sumSquaredDigits(num: int) -> int:
	res = 0
	while num > 0:
		digit = num % 10
		res += digit ** 2
		num = num // 10
	return res

print(isHappy(2))
