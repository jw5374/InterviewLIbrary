# binary tree consists of exactly 3 nodes
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def checkTree(root: TreeNode) -> bool:
	return root.left.val + root.right.val == root.val

testRoot = TreeNode(10)
leftNode = TreeNode(4)
rightNode = TreeNode(6)

testRoot.left = leftNode
testRoot.right = rightNode

print(checkTree(testRoot))
