# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root: TreeNode) -> list[float]:
    nodeStack = [[root]]
    res = []
    while len(nodeStack) > 0:
        currLev = nodeStack.pop()
        currSum = 0
        nextLev = []
        for node in currLev:
            currSum += node.val
            if node.left is not None:
                nextLev.append(node.left)
            if node.right is not None:
                nextLev.append(node.right)
        if len(nextLev) > 0:
            nodeStack.append(nextLev)
        res.append(currSum / len(currLev))
    return res
