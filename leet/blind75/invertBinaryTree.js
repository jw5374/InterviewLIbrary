const { treeGen, TreeNode } = require('../viewLib/forest.js')

function invertTree(root) {
  if(root == null) {
    return root
  }
  let temp = root.left
  root.left = root.right
  root.right = temp
  invertTree(root.left)
  invertTree(root.right)
  return root
}

let vals = [4,2,7,1,3,6,9]
let nodes = []
for(let val of vals) {
  nodes.push(val == null ? null : new TreeNode(val))
}

let tree = treeGen(nodes)
console.log(tree)
invertTree(tree)
console.log(tree)
