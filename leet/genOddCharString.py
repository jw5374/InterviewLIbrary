import random

def generateTheString(n: int) -> str:
	res = ""
	if n % 2 == 0:
		res += chr(random.randint(97, 109)) * (n-1)
		res += chr(random.randint(110, 122))
	else:
		res += chr(random.randint(97, 122)) * n
	return res

print(generateTheString(26))
