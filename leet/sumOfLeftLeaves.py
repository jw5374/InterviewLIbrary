class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def sumOfLeftLeaves(root: TreeNode) -> int:
    return sumLeft(root, 0) if not checkLeaf(root) else 0


def sumLeft(node: TreeNode, sum: int) -> int:
    if checkLeaf(node):
        return node.val
    if node.right is not None and not checkLeaf(node.right):
        sum += sumLeft(node.right, 0)
    if node.left is not None:
        sum += sumLeft(node.left, 0)
    return sum


def checkLeaf(node: TreeNode) -> bool:
    return (node.left is None and node.right is None)

