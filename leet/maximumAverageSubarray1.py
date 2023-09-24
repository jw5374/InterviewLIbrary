def findMaxAverage(nums: list[int], k: int) -> float:
    [i, j] = [0, k-1]
    currSum = sum(nums[i:j+1])
    currAvg = currSum / k
    while j < len(nums) - 1:
        currSum -= nums[i]
        currSum += nums[j+1]
        i += 1
        j += 1
        avg = currSum / k
        if avg > currAvg:
            currAvg = avg
    return currAvg
