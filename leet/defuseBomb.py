def decrypt(code: list[int], k: int):
	if(k == 0):
		return [0 for num in code]
	res = []
	keySign = k < 0
	for i in range(len(code)):
		sliced = (
			(code[i+1:i+k+1], code[i+1:] + code[0:k-(len(code)-(i+1))])[i+k >= len(code)],
			(code[i+k:i], code[0:i] + code[len(code)-(-k-i):])[i+k < 0]
		)[keySign]
		res.append(sum(sliced))
	return res

print(decrypt([5,7,1,4], 3))
