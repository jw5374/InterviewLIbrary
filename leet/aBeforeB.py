def checkString(s: str) -> bool:
	if len(s) == 1:
		return True
	[left, right] = [0, len(s)-1]
	while right > 0 and s[right] != "a":
		right -= 1
	if right == 0:
		return True
	while left <= right:
		if s[left] != "a" or s[right] != "a":
			return False
		left += 1
		right -=1
	return True

print(checkString("ababb"))
