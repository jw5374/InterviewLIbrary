from typing import List


"""
nums: array of nums
k: current index to swap (starts as length of nums - 1)
"""
def generatePermutation(nums: List[int], k: int) -> List[List[int]]:
    res = []
    # reaching the head of array, return current state
    if k == 0:
        return [nums.copy()]

    # generate permutations for if current index is not swapped
    res += generatePermutation(nums.copy(), k - 1)

    # generate permutation for swaps on current index
    for i in range(k):

        # if current index is even then swap with each element
        if k % 2 == 0:
            nums[i], nums[k] = nums[k], nums[i]

        # otherwise always swap with head
        else:
            nums[0], nums[k] = nums[k], nums[0]
        res += generatePermutation(nums.copy(), k - 1)
    return res

# generatePermutation([1,2,3], 2)
print(generatePermutation([1,2,3], 2))


def generateIterPermut(nums: List[int]) -> List[List[int]]:
    res = []

    # simulates k inside recursive for loop
    kSim = [0] * len(nums)

    res.append(nums.copy())
    
    i = 0
    while i < len(nums):

        # simulates an inner loop until corresponding k value
        if kSim[i] < i:
            
            # same as recursive
            if i % 2 == 0:
                nums[0], nums[i] = nums[i], nums[0]
            else:
                nums[i], nums[kSim[i]] = nums[kSim[i]], nums[i]
            res.append(nums.copy())

            # increment the k and reset where our i is to initiate a re-loop
            kSim[i] += 1
            i = 0
        else:

            # reset the state and increment our i
            kSim[i] = 0
            i += 1
    return res


print(generateIterPermut([1,2,3]))

