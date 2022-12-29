def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    if n == 1 or (source == destination):
        return True
    adjList = {}
    for edge in edges:
        directEdge = (edge[0] == source and edge[1] == source) or (edge[1] == source and edge[0] == source)
        if directEdge:
            return True
        if edge[0] in adjList and edge[1] in adjList:
            adjList[edge[1]].append(edge[0])
            adjList[edge[0]].append(edge[1])
            continue
        if edge[0] in adjList:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]] = [edge[0]]
            continue
        if edge[1] in adjList:
            adjList[edge[1]].append(edge[0])
            adjList[edge[0]] = [edge[1]]
            continue
        adjList[edge[0]] = [edge[1]]
        adjList[edge[1]] = [edge[0]]
    visited = {}
    nodes = adjList[source]
    while len(nodes) > 0:
        visiting = nodes.pop(0)
        if visiting in visited:
            continue
        if visiting == destination:
            return True
        visited[visiting] = True
        for node in adjList[visiting]:
            if node == source:
                continue
            nodes.append(node)
    return False


print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))

