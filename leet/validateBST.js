const { nodeGen } = require('../viewLib/forest.js')
function isValidBST(root, min=Number.MIN_SAFE_INTEGER, max=Number.MAX_SAFE_INTEGER) {
    if(root == null) {
        return true
    }
    if(root.val <= min || root.val >= max) {
        return false
    }
    if(root.left != null && root.left.val >= root.val) {
        return false
    }
    if(root.right != null && root.right.val <= root.val) {
        return false
    }
    if(!isValidBST(root.left, min, root.val) || !isValidBST(root.right, root.val, max)) {
        return false
    }
    return true 
}
let nodes = nodeGen(1)
nodes[0].val = 0
console.log(isValidBST(nodes[0]))
