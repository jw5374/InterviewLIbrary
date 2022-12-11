import re

# 's' must be of even length (defined by leetcode)
def halvesAreAlike(s: str) -> bool:
	lowered = s.lower()
	regex = "[aeiou]+"
	sLen = len(lowered)
	halves = [lowered[0:sLen//2], lowered[sLen//2:]]
	return len(returnRegexMatch(regex, halves[0])) == len(returnRegexMatch(regex, halves[1]))

def returnRegexMatch(exp: str, string: str) -> str:
	return "".join(re.findall(exp, string))

print(halvesAreAlike("MerryChristmas"))
