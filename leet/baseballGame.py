def calPoints(operations: list[str]) -> int:
    recs = []
    for op in operations:
        if op.lstrip("-").isdigit():
            recs.append(int(op))
        elif op == "C":
            recs.pop()
        elif op == "D":
            recs.append(recs[-1] * 2)
        elif op == "+":
            recs.append(recs[-1] + recs[-2])
        print(recs)
    return sum(recs)
