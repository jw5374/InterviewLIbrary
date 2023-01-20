class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluateTree(root: TreeNode) -> bool:
    if root.val <= 1:
        return bool(root.val)
    if root.val == 2:
        return evaluateTree(root.left) or evaluateTree(root.right)
    return evaluateTree(root.left) and evaluateTree(root.right)

