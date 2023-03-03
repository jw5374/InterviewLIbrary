def lastStoneWeight(stones: list[int]) -> int:
    while len(stones) > 1:
        stones.sort()
        if stones[-1] != stones[-2]:
            destroyed = stones.pop(-2)
            stones[-1] -= destroyed
        else:
            stones.pop()
            stones.pop()
    return stones[0] if len(stones) > 0 else 0


print(lastStoneWeight([2,7,4,1,8,1]))

