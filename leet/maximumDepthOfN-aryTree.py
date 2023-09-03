# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(self, root: Node) -> int:
    if len(root.children) == 0:
        return 1
    res = 0
    for child in root.children:
        res = max(res, 1 + self.maxDepth(child))
    return res
