def distributeCandies(candies: int, num_people: int) -> list[int]:
    i = 0
    give = 1
    res = [0] * num_people
    while candies > 0:
        if give >= candies:
            res[i] += candies
            break
        res[i] += give
        candies -= give
        give += 1
        if i < num_people-1:
            i += 1
        else:
            i = 0
    return res


print(distributeCandies(10, 3))

