def distributeCandies(candyType: list[int]) -> int:
    uniques = len(set(candyType))
    full = len(candyType) // 2
    return uniques if uniques <= full else full
