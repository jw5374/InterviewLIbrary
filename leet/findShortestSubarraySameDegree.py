def findShortestSubArray(nums: list[int]) -> int:
    numOccs = {}
    greatestOcc = [-1, []]
    for i, num in enumerate(nums):
        if num in numOccs:
            numOccs[num].append(i)
        else:
            numOccs[num] = [i]
        if greatestOcc[0] < len(numOccs[num]):
            greatestOcc[0] = len(numOccs[num])
            greatestOcc[1] = numOccs[num]
        elif greatestOcc[0] == len(numOccs[num]):
            if greatestOcc[1][-1] - greatestOcc[1][0] > numOccs[num][-1] - numOccs[num][0]:
                greatestOcc[1] = numOccs[num]
    return (greatestOcc[1][-1] - greatestOcc[1][0]) + 1
