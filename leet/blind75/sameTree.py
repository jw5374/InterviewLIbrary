class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    pStack = [p]
    qStack = [q]
    if p is None and q is None:
        return True
    while len(pStack) > 0 and len(qStack) > 0:
        [pNode, qNode] = [pStack.pop(), qStack.pop()]
        if (pNode is None and qNode is not None) or (pNode is not None and qNode is None):
            return False
        if (pNode.left is None and qNode.left is not None) or (pNode.left is not None and qNode.left is None):
            return False
        if (pNode.right is None and qNode.right is not None) or (pNode.right is not None and qNode.right is None):
            return False
        if pNode is not None and qNode is not None:
            if pNode.val != qNode.val:
                return False
            if pNode.left is not None:
                pStack.append(pNode.left)
            if pNode.right is not None:
                pStack.append(pNode.right)
            if qNode.left is not None:
                qStack.append(qNode.left)
            if qNode.right is not None:
                qStack.append(qNode.right)
    return True

