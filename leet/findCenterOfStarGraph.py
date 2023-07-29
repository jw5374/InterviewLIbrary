def findCenter(edges: list[list[int]]) -> int:
    nodes = {}
    for edge in edges:
        if edge[0] in nodes:
            nodes[edge[0]] += 1
        else:
            nodes[edge[0]] = 1
        if edge[1] in nodes:
            nodes[edge[1]] += 1
        else:
            nodes[edge[1]] = 1
    for node, occ in nodes.items():
        if occ == len(edges):
            return node
