def finalPrices(prices: list[int]) -> list[int]:
	stack = []
	for i in range(len(prices)):
		while len(stack) != 0 and prices[stack[-1]] >= prices[i]:
			prices[stack.pop()] -= prices[i]
		stack.append(i)
	return prices

print(finalPrices([8,7,4,2,8,1,7,7,10,1]))
