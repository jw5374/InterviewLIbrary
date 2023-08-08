# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: TreeNode) -> list[int]:
    nodeStack = [root]
    occs = {}
    while len(nodeStack) > 0:
        curr = nodeStack.pop()
        if curr.val in occs:
            occs[curr.val] += 1
        else:
            occs[curr.val] = 1
        if curr.left is not None:
            nodeStack.append(curr.left)
        if curr.right is not None:
            nodeStack.append(curr.right)
    modeOcc = 0
    for occ in occs.values():
        if modeOcc < occ:
            modeOcc = occ
    for val in occs.keys():
        if occs[val] == modeOcc:
            nodeStack.append(val)
    return nodeStack
