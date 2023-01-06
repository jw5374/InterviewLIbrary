def findRelativeRanks(score: list[int]) -> list[str]:
    top = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    sorted = score.copy()
    sorted.sort(reverse=True)
    indices = {}
    for i, val in enumerate(score):
        indices[val] = i
    for i, val in enumerate(sorted):
        if i < 3:
            score[indices[val]] = top[i]
        else:
            score[indices[val]] = str(i + 1)
    return score


print(findRelativeRanks([5,4,3,2,1]))

