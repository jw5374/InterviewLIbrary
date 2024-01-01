import math

# taken E12.js
def findNaturalFactors(num: int) -> list[int]:
	factors = []
	for i in range(2, math.floor(math.sqrt(num))):
		if num % i == 0:
			if(num // i != 1):
				factors.append(i)
				factors.append(num//i)
	return factors

# naive quadratic
def amicableNumSum(maxNum: int) -> int:
	totalNumSum = 0
	for i in range(2, maxNum):
		firstFactors = sum(findNaturalFactors(i)) + 1
		secondSum = sum(findNaturalFactors(firstFactors)) + 1
		if i == secondSum and i != firstFactors:
			print(i)
			totalNumSum += i
		# for j in range(i+1, maxNum):
		# 	secondFactors = sum(findNaturalFactors(j))
		# 	if firstFactors == secondFactors:
		# 		totalNumSum += i + j
		# 		break
	return totalNumSum

print(amicableNumSum(10001))
