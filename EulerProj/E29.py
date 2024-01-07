# for a ^ b find all distinct products with combinations
# 2 <= a <= 1000, 2 <= b <= 1000
# sanity check: range is reduced to 5

# quadratic complexity :(
def distinctPowers(upperRange: int) -> set[int]:
	powers = set()
	for i in range(2, upperRange+1):
		for j in range(2, upperRange+1):
			powers.add(i ** j)
	return len(powers)

print(distinctPowers(100))
