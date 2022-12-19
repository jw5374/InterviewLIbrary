def mergeSimilarItems(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
	fullItems = items1 + items2
	fullItems.sort(key=lambda item: item[0])
	res = []
	i = 0
	while i < len(fullItems):
		local = fullItems[i]
		while i < len(fullItems) - 1 and local[0] == fullItems[i+1][0]:
			local[1] += fullItems[i+1][1]
			i += 1
		res.append(local)
		i += 1
	return res

def mergeHashed(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
	hash = {}
	res = []
	for val, weight in (items1 + items2):
		if val in hash:
			hash[val] += weight
		else:
			hash[val] = weight
	for key, val in hash.items():
		res.append([key, val])

	# still need to sort T_T
	res.sort(key=lambda item: item[0])
	return res

print(mergeHashed([[1,3],[2,2]], [[7,1],[2,2],[1,4]]))
