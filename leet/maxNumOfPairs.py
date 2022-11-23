def numberOfPairs(nums):
    res = [0, 0]
    hash = {}
    for i in range(len(nums)):
        if(nums[i] in hash):
            hash[nums[i]] += 1
        else:
            hash[nums[i]] = 1
    for val in hash.values():
        if(val % 2 == 0):
            res[0] += val // 2
        else:
            res[0] += val // 2
            res[1] += val % 2
    return res
    
print(numberOfPairs([0]))
    