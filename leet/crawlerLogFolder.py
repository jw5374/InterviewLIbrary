def minOperations(logs: list[str]) -> int:
    ops = 0
    for log in logs:
        if log == "../":
            ops = ops - 1 if ops > 0 else ops
        elif log == "./":
            continue
        else:
            ops += 1
    return ops


print(minOperations(["d1/","d2/","../","d21/","./"]))

