class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def minDepth(root: TreeNode) -> int:
	if root == None:
		return 0
	if root.left == None and root.right == None:
		return 1
	leftDepth = math.inf
	rightDepth = math.inf
	if root.left != None:
		leftDepth = self.minDepth(root.left)
	if root.right != None:
		rightDepth = self.minDepth(root.right) 
	return 1 + min(leftDepth, rightDepth)
