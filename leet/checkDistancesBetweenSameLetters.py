def checkDistances(self, s: str, distance: list[int]) -> bool:
    visited = {}
    for i, c in enumerate(s):
        if c in visited:
            flag = distance[ord(c) - 97] == i - visited[c] - 1
            if not flag:
                return False
            del visited[c]
        else:
            visited[c] = i
    return True
