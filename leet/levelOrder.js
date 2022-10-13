const { treeGen, TreeNode } = require('../viewLib/forest.js')

function levelOrder(root) {
    if(root == null) {
      return []
    }
    let result = []
    let stack = [[root]]
    while(stack.length > 0) {
        let layerVals = []
        let stackLayer = []
        let layer = stack.pop()
        for(let node of layer) {
            layerVals.push(node.val) 
            if(node.left != null) {
                stackLayer.push(node.left)
            }
            if(node.right != null) {
                stackLayer.push(node.right)
            }
        }
        if(stackLayer.length > 0) {
          stack.push(stackLayer)
        }
        result.push(layerVals)
    }
    return result
}

let nodevals = [3,9,20,null,null,15,7]
let nodes = []
for(let val of nodevals) {
  nodes.push(val == null ? null : new TreeNode(val))
}

let tree = treeGen(nodes)

console.log(tree)
console.log(levelOrder(tree))
