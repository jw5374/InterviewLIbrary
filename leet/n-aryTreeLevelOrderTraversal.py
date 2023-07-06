class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: Node) -> list[list[int]]:
    if root is None:
        return []
    nodeStack = [[root]]
    res = []
    while len(nodeStack) > 0:
        currLevel = nodeStack.pop()
        resVals = []
        nextLevel = []
        for n in currLevel:
            resVals.append(n.val)
            nextLevel += n.children if n.children is not None else []
        if len(nextLevel) > 0:
            nodeStack.append(nextLevel)
        res.append(resVals)
    return res


tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(levelOrder(tree))
