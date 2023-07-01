# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: TreeNode) -> list[int]:
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]
