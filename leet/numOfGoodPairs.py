def numIdenticalPairs(nums: list[int]) -> int:
    found = {}
    res = 0
    for i, num in enumerate(nums):
        if num not in found:
            found[num] = [i]
        else:
            res += len(found[num])
            found[num].append(i)
    # for indexes in found.values():
    #     if len(indexes) > 1:
    #         res += math.comb(len(indexes), 2)
    return res
