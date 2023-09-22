def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
    for row in image:
        [i, j] = [0, len(row) - 1]
        while i <= j:
            if i == j:
                row[i] = 1 - row[i]
                break
            row[i] = 1 - row[i]
            row[j] = 1 - row[j]
            row[i], row[j] = row[j], row[i]
            i += 1
            j -= 1
    return image
