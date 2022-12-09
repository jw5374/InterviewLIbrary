import math

def isPowerOfThree(n: int) -> bool:
	if n <= 0:
		return False
	cblog = math.log(n, 3)  # LOGS ARE INACCURATE NOT MY FAULT >:(
	return 3 ** math.ceil(cblog) == n or 3 ** math.floor(cblog) == n

def linearPowerOfThree(n: int) -> bool:
	while n > 1:
		if n % 3 != 0:
			return False
		n = n // 3
	return True

print(linearPowerOfThree(1162261467))
