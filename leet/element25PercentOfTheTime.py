def findSpecialInteger(arr: list[int]) -> int:
    limit = len(arr) // 4
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr) and arr[i] == arr[j]:
            j += 1
        if j - i > limit:
            return arr[i]
