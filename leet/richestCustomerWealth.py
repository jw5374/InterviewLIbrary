def maximumWealth(accounts: list[list[int]]) -> int:
    res = 0
    for account in accounts:
        res = max(res, sum(account))
    return res


print(maximumWealth([[1,2,3],[3,2,1]]))

