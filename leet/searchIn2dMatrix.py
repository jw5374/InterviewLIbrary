def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    [low, high] = [0, len(matrix) - 1]
    while low < high:
        mid = (low + high) // 2
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] < target and matrix[mid][-1] >= target:
            low = mid
            break
        if matrix[mid][0] < target:
            low = mid + 1
        if matrix[mid][0] > target:
            high = mid - 1
    [rowLow, rowHigh] = [0, len(matrix[low]) - 1]
    while rowLow <= rowHigh:
        mid = (rowLow + rowHigh) // 2
        if matrix[low][mid] == target:
            return True
        if matrix[low][mid] < target:
            rowLow = mid + 1
        if matrix[low][mid] > target:
            rowHigh = mid - 1
    return False
