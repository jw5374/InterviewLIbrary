def constructRectangle(area: int) -> list[int]:
    for i in range(int((area ** 0.5) // 1), 0, -1):
        if area % i != 0:
            continue
        return [area // i, i]
