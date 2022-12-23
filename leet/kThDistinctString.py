def kthDistinct(arr: list[str], k: int) -> str:
	hash = {}
	for i, s in enumerate(arr):
		if s in hash:
			hash[s] = False
		else:
			hash[s] = i
	i = 0
	while i < len(arr) and k > 0:
		if hash[arr[i]] is not False:
			k -= 1
		i += 1
	return arr[i-1] if k <= 0 else ""

print(kthDistinct(["a","b","a"], 3))
