class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> list[int]:
    trav = []
    getTraversal(root, trav)
    return trav


def getTraversal(root: TreeNode, order: list[int]) -> None:
    if root is None:
        return
    if root.left is not None:
        getTraversal(root.left, order)
    order.append(root.val)
    if root.right is not None:
        getTraversal(root.right, order)

