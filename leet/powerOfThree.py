import math

def isPowerOfThree(n: int) -> bool:
	if n <= 0:
		return False
	cblog = math.log(n, 3)  # LOGS ARE INACCURATE NOT MY FAULT >:(
	return 3 ** math.ceil(cblog) == n or 3 ** math.floor(cblog) == n

print(isPowerOfThree(1162261467))
