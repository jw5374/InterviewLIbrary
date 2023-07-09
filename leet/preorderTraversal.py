class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: TreeNode) -> list[int]:
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


def preorderTraversalIter(root: TreeNode) -> list[int]:
    if root is None:
        return []
    nodeStack = [root]
    res = []
    while len(nodeStack) > 0:
        currNode = nodeStack.pop()
        res.append(currNode.val)
        if currNode.right is not None:
            nodeStack.append(currNode.right)
        if currNode.left is not None:
            nodeStack.append(currNode.left)
    return res
    
