def timeRequiredToBuy(tickets: list[int], k: int) -> int:
    total = 0
    for i in range(len(tickets)):
        if tickets[i] >= tickets[k]:
            total += tickets[k]
            if i > k:
                total -= 1
        else:
            total += tickets[i]
    return total

