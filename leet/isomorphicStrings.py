# s and t have same lengths as defined by problem statement
def isIsomorphic(s: str, t: str) -> bool:
	hash = {}
	for i in range(len(s)):
		[sVal, tVal] = [s[i]+"_", t[i]]
		if sVal not in hash and tVal not in hash:
			hash[sVal] = t[i]
			hash[tVal] = s[i]
		elif hash.get(sVal) != t[i] or hash.get(tVal) != s[i]:
			return False
	return True

print(isIsomorphic("add", "egg"))
