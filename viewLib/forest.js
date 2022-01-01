class TreeNode {
    constructor(val, left, right) {
        this.val = val ? val : null
        this.left = left ? left : null
        this.right = right ? right : null
    }
}

function nodeGen(nodeCount) {
    let nodes = []
    for(let i = 0; i < nodeCount; i++) {
        nodes.push(new TreeNode(i+1))
    }
    return nodes
}

function treeGen(nodes) {
    for(let i = 0; i < nodes.length; i++) {
        let left = 2*i + 1
        let right = 2*i + 2
        if(left < nodes.length) {
            nodes[i].left = nodes[left]
        }
        if(right < nodes.length) {
            nodes[i].right = nodes[right]
        }
        if(left >= nodes.length || right >= nodes.length) {
            break
        }
    }
    return nodes.shift()
}

function preorderTraverse(treeRoot, sequence) {
    if(treeRoot.left == null && treeRoot.right == null) {
        sequence.push(treeRoot.val)
        return
    }
    sequence.push(treeRoot.val)
    if(treeRoot.left != null) {
        preorderTraverse(treeRoot.left, sequence)
    }
    if(treeRoot.right != null) {
        preorderTraverse(treeRoot.right, sequence)
    }
}

function postorderTraverse(treeRoot, sequence) {
    if(treeRoot.left == null && treeRoot.right == null) {
        sequence.push(treeRoot.val)
        return
    }
    if(treeRoot.left != null) {
        postorderTraverse(treeRoot.left, sequence)
    }
    if(treeRoot.right != null) {
        postorderTraverse(treeRoot.right, sequence)
    }
    sequence.push(treeRoot.val)
}

function inorderTraverse(treeRoot, sequence) {
    if(treeRoot.left == null && treeRoot.right == null) {
        sequence.push(treeRoot.val)
        return
    }
    if(treeRoot.left != null) {
        inorderTraverse(treeRoot.left, sequence)
    }
    sequence.push(treeRoot.val)
    if(treeRoot.right != null) {
        inorderTraverse(treeRoot.right, sequence)
    }
}

function breadthFirst(treeRoot, sequence, queue = []) {
    if(treeRoot == null) {
        return
    }
    if(treeRoot != null && treeRoot.val != "visited") {
        queue.push([treeRoot.val, treeRoot])
        treeRoot.val = "visited"
    }
    if(treeRoot.left != null && treeRoot.left.val != "visited") {
        queue.push([treeRoot.left.val, treeRoot.left])
        treeRoot.left.val = "visited"
    }
    if(treeRoot.right != null && treeRoot.right.val != "visited") {
        queue.push([treeRoot.right.val, treeRoot.right])
        treeRoot.right.val = "visited"
    }
    if(queue.length == 0) {
        return
    }
    if(treeRoot.left == null || treeRoot.right == null) {
        let pop = queue.shift()
        sequence.push(pop[0])
        breadthFirst(pop[1], sequence, queue)
        return
    }
    if(treeRoot.left.val == "visited" && treeRoot.right.val == "visited") {
        let pop = queue.shift()
        sequence.push(pop[0])
        breadthFirst(pop[1], sequence, queue)
    }
}



module.exports = { nodeGen, treeGen, preorderTraverse, postorderTraverse, inorderTraverse, breadthFirst }