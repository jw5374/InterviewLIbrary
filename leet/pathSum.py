class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if root is None:
        return False
    if (root.left is None and root.right is None) and (targetSum - root.val == 0):
        return True
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

