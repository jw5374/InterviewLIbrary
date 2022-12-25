def destCity(paths: list[list[str]]) -> str:
    adjList = {}
    for path in paths:
        if path[0] not in adjList:
            adjList[path[0]] = True
    for path in paths:
        if path[1] not in adjList:
            return path[1]


print(destCity([["B","C"],["D","B"],["C","A"]]))

