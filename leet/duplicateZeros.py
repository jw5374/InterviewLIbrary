def duplicateZeros(arr: list[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    copy = arr.copy()
    [i, j] = [0, 0]
    while i < len(arr):
        arr[i] = copy[j]
        if i < len(arr) - 1 and copy[j] == 0:
            arr[i+1] = 0
            i += 2
        else:
            i += 1
        j += 1
