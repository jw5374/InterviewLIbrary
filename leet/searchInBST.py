class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root.val == val:
        return root
    if root.val < val and root.left is not None:
        return searchBST(root.left, val)
    if root.val > val and root.right is not None:
        return searchBST(root.right, val)
    return None

