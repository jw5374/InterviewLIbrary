# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode) -> bool:
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    leftPath = longestPath(root.left)
    rightPath = longestPath(root.right)
    if abs(rightPath - leftPath) <= 1:
        return isBalanced(root.left) and isBalanced(root.right)
    return False


def longestPath(node: TreeNode) -> int:
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return max(1 + longestPath(node.left), 1 + longestPath(node.right))
