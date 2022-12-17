def toLowerCase(s: str) -> str:
	return "".join([toLowerAscii(c) for c in s])

def toLowerAscii(s: str) -> str:
	if ord(s) - 64 <= 26 and ord(s) - 64 >= 1:
		return chr(ord(s) + 32)
	else:
		return s

print(toLowerCase("here"))
