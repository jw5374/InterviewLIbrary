class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isUnivalTree(root: TreeNode) -> bool:
    curVal = root.val
    nodes = [root]
    while len(nodes) > 0:
        curNode = nodes.pop()
        if curVal != curNode.val:
            return False
        if curNode.left is not None:
            nodes.append(curNode.left)
        if curNode.right is not None:
            nodes.append(curNode.right)
    return True

