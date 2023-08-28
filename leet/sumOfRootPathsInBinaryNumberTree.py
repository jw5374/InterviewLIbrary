class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumRootToLeaf(self, root: TreeNode) -> int:
    res = 0
    for path in returnPaths(root, ""):
        res += int(path, 2)
    return res


def returnPaths(root: TreeNode, currPath: str) -> list[str]:
    if root.left is None and root.right is None:
        return [currPath + str(root.val)]
    [left, right] = [[], []]
    if root.left is not None:
        left = returnPaths(root.left, currPath + str(root.val))
    if root.right is not None:
        right = returnPaths(root.right, currPath + str(root.val))
    return left + right
