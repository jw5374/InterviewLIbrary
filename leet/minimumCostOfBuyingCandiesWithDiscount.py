def minimumCost(cost: list[int]) -> int:
    cost.sort()
    sum = 0
    for i in range(len(cost) - 1, -1, -3):
        sum += cost[i] + (cost[i-1] if i > 0 else 0)
    return sum
