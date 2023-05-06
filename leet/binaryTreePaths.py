# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: TreeNode) -> list[str]:
    if root is None:
        return []
    if root.right is None and root.left is None:
        return [str(root.val)]
    allPaths = binaryTreePaths(root.left) + binaryTreePaths(root.right)
    currPaths = []
    for path in allPaths:
        currPaths.append(f"{str(root.val)}->{path}")
    return currPaths
