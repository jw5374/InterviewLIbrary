def findJudge(n: int, trust: list[list[int]]) -> int:
    inbound = [set() for i in range(n)]
    outbound = [set() for i in range(n)]
    for edge in trust:
        inbound[edge[1] - 1].add(edge[0] - 1)
        outbound[edge[0] - 1].add(edge[1] - 1)
    for i, nodes in enumerate(inbound):
        if len(nodes) != (n - 1):
            continue
        if len(outbound[i]) == 0:
            return i + 1
    return -1
