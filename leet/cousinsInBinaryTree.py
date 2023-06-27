class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isCousins(root: TreeNode, x: int, y: int) -> bool:
    levels = {}
    nodeStack = [[[root, TreeNode(val=-1)]]]
    i = 1
    while len(nodeStack) > 0:
        curr = nodeStack.pop()
        currLevel = []
        for node in curr:
            currNode = node[0]
            levels[currNode.val] = [i, node[1]]
            if currNode.left is not None:
                currLevel.append([currNode.left, currNode])
            if currNode.right is not None:
                currLevel.append([currNode.right, currNode])
        if len(currLevel) > 0:
            nodeStack.append(currLevel)
        i += 1
    levelX = levels[x]
    levelY = levels[y]
    print(levels)
    return levelX[0] == levelY[0] and levelX[1].val != levelY[1].val


root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=None), right=TreeNode(val=3))
print(isCousins(root, 4, 3))
