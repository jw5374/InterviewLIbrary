const { treeGen, TreeNode } = require('../viewLib/forest.js')

function maxDepth(root) {
  if(root == null) {
    return 0
  }
  if(root.left == null && root.right == null) {
    return 1
  }
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right))
}

let vals = [3,9,20,null,null,15,7]
let nodes = []
for(let val of vals) {
  nodes.push(val == null ? null : new TreeNode(val))
}

let tree = treeGen(nodes)
console.log(maxDepth(tree))
