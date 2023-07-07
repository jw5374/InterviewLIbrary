class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorderRecursive(root: Node) -> list[int]:
    if root is None:
        return []
    if root.children is None:
        return [root.val]
    res = []
    for child in root.children:
        res += preorderRecursive(child)
    return [root.val] + res


def preorderIter(root: Node) -> list[int]:
    if root is None:
        return []
    nodeStack = [root]
    res = []
    while len(nodeStack) > 0:
        currNode = nodeStack[-1]
        res.append(currNode.val)
        nodeStack.pop()
        while currNode.children is not None and len(currNode.children) > 0:
            for i in range(len(currNode.children) - 1, -1, -1):
                nodeStack.append(currNode.children.pop())
            currNode = nodeStack[-1]
            res.append(currNode.val)
            nodeStack.pop()
    return res


tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(preorderIter(tree))
