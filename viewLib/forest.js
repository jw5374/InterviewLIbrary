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

function preorderTraverse(treeRoot) {
    if(treeRoot == null) {
        return []
    }

    let left = preorderTraverse(treeRoot.left)
    let right = preorderTraverse(treeRoot.right)
    return [treeRoot.val, ...left, ...right]
}

function preorderTraverseIter(treeRoot, nodeStack = []) {
    let sequence = []
    nodeStack.push(treeRoot)
    while(nodeStack.length > 0) {
        let currNode = nodeStack.pop()
        sequence.push(currNode.val)
        if(currNode.right != null) {
            nodeStack.push(currNode.right)
        }
        if(currNode.left != null) {
            nodeStack.push(currNode.left)
        }
    }
    return sequence
}

function postorderTraverse(treeRoot) {
    if(treeRoot == null) {
        return []
    }

    let left = postorderTraverse(treeRoot.left)
    let right = postorderTraverse(treeRoot.right)
    return [...left, ...right, treeRoot.val]
}

function inorderTraverse(treeRoot) {
    if(treeRoot == null) {
        return []
    }

    let left = inorderTraverse(treeRoot.left)
    let right = inorderTraverse(treeRoot.right)
    return [...left, treeRoot.val ,...right]
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

function breadthFirstIter(treeRoot, queue = []) {
    let sequence = []
    queue.push(treeRoot)
    while(queue.length > 0) {
        let node = queue.shift()
        sequence.push(node.val)
        if(node.left != null) {
            queue.push(node.left)
        }
        if(node.right != null) {
            queue.push(node.right)
        }
    }
    return sequence
}

module.exports = { TreeNode, nodeGen, treeGen, preorderTraverse, postorderTraverse, inorderTraverse, breadthFirst, breadthFirstIter, preorderTraverseIter }