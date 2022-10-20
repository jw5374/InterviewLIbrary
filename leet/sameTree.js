const { treeGen, TreeNode } = require('../viewLib/forest.js')

function isSameTree(p, q) {
  if(p == null && q == null) {
    return true
  }
  if((p == null && q != null) || (p != null && q == null)) {
    return false
  }
  if(p.val != q.val) {
    return false
  }
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
}


let vals = [1,2,1]
let vals2 = [1,1,2]
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
// console.log(isSameTree(tree, tree2))
 
module.exports = { isSameTree }
