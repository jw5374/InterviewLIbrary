const { isSameTree } = require('./sameTree.js')
const { treeGen, TreeNode } = require('../viewLib/forest.js')

function isSubtree(root, subroot) {
  if(root == null || subroot == null) {
    return false
  }
  if(isSameTree(root, subroot)) {
    return true
  }  
  if(isSubtree(root.left, subroot) || isSubtree(root.right, subroot)) {
    return true
  }
  return false
}

let vals = [3,4,5,1,2]
let vals2 = [4,1,2]
let nodes = []
let nodes2 = []
for(let val of vals) {
  nodes.push(val == null ? null : new TreeNode(val))
}
for(let val of vals2) {
  nodes2.push(val == null ? null : new TreeNode(val))
}

let tree = treeGen(nodes)
let tree2 = treeGen(nodes2)
console.log(isSubtree(tree, tree2))
