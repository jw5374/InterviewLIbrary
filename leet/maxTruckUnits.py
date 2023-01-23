def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    res = 0
    for box in boxTypes:
        if truckSize <= 0:
            break
        if box[0] > truckSize:
            res += box[1] * truckSize
            break
        res += box[0] * box[1]
        truckSize -= box[0]
    return res


print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))

