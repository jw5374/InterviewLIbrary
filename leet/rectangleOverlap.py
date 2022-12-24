def isRectangleOverlap(rec1: list[int], rec2: list[int]) -> bool:
    oneAbove = (rec1[1] >= rec2[3]) or (rec2[1] >= rec1[3])
    oneLeft = (rec1[2] <= rec2[0]) or (rec2[2] <= rec1[0])
    return not (oneAbove or oneLeft)


print(isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))

