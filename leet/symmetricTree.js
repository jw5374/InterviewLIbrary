const { TreeNode, treeGen } = require('../viewLib/forest.js') 

function isPalindrome(arr) {
  let [i,j] = [0, arr.length-1]
  while(i < j) {
    if(arr[i] != arr[j]) {
      return false
    }
    i++
    j--
  }
  return true
}

function isSymmetric(root) {
  let level = [root]
  while(level.length > 0) {
    let stackLayer = []
    let stackNodes = []
    for(let node of level) {
      stackLayer.push(node == null ? null : node.val)
      if(node == null) {
        continue
      }
      stackNodes.push(node.left)
      stackNodes.push(node.right)
    }
    if(!isPalindrome(stackLayer)) {
      return false
    }
    level = stackNodes
  }
  return true
}

let vals = [1,2,2,null,3,null,3]
let nodes = []
for(let val of vals) {
  nodes.push(val == null ? null : new TreeNode(val))
}

let tree = treeGen(nodes)
console.log(tree)
console.log(isSymmetric(tree))
