# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: TreeNode) -> int:
    nodes = [root]
    maxPath = -1
    while len(nodes) > 0:
        curr = nodes.pop()
        if curr.left is not None:
            nodes.append(curr.left)
        if curr.right is not None:
            nodes.append(curr.right)
        maxPath = max(maxPath, longestPath(curr.left) + longestPath(curr.right))
    return maxPath


def longestPath(root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return max(1 + longestPath(root.left), 1 + longestPath(root.right))
