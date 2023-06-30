# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    first = leafSequence(root1)
    second = leafSequence(root2)
    if len(first) != len(second):
        return False
    for i, num in enumerate(first):
        if second[i] != num:
            return False
    return True


def leafSequence(root: TreeNode) -> list[int]:
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    return leafSequence(root.left) + leafSequence(root.right)
