exports.arrayGen = function arrayGen(n) {
    let array = [...Array(n+1).keys()]
    array.shift() 
    return array
}

exports.matrixGen = function matrixGen(m, n, fillVal = 0) {
    let matrix = []
    for(let i = 0; i < m; i++) {
        matrix.push([...Array(n).fill(fillVal)])
    }
    return matrix
}

exports.randomArrayGen = function randomArrayGen(n, maxVal) {
    let array = []
    while(array.length < n) {
        let num = Math.floor(Math.random() * maxVal) + 2
        if(num in array) {
            continue
        } else {
            array.push(num)
        }
    }
    return array
}

exports.shuffle = function shuffle(array) {
    let swapIndex, min
    let max = array.length
    for(let i = 0; i < array.length - 1; i++) {
        min = i+1
        swapIndex = Math.floor(Math.random() * (max - min) + min)
        let temp = array[i]
        array[i] = array[swapIndex]
        array[swapIndex] = temp
    }
}

exports.swap = function swap(a, b, array) {
    let temp = array[a]
    array[a] = array[b]
    array[b] = temp
}

exports.mergeSorted = function mergeSorted(array1, array2) {
    let merged = []
    let i = 0, j = 0
    while(i < array1.length) {
        if(array1[i] >= array2[j]) {
            merged.push(array2[j++])
        } else {
            merged.push(array1[i++])
        }
    }
    while(j < array2.length) {
        merged.push(array2[j++])
    }
    return merged
}

exports.maxHeapify = function maxHeapify(arr, index) {
    let largest
    let leftNode = (index * 2) + 1
    let rightNode = (index * 2) + 2
    if(leftNode < arr.length && arr[leftNode] > arr[index]) {
        largest = leftNode
    } else {
        largest = index
    }
    if(rightNode < arr.length && arr[rightNode] > arr[largest]) {
        largest = rightNode
    }
    if(largest != index) {
        module.exports.swap(index, largest, arr)
        maxHeapify(arr, largest)
    }
}

exports.minHeapify = function minHeapify(arr, index) {
    let smallest
    let leftNode = (index * 2) + 1
    let rightNode = (index * 2) + 2
    if(leftNode < arr.length && arr[leftNode] < arr[index]) {
        smallest = leftNode
    } else {
        smallest = index
    }
    if(rightNode < arr.length && arr[rightNode] < arr[smallest]) {
        smallest = rightNode
    }
    if(smallest != index) {
        module.exports.swap(index, smallest, arr)
        minHeapify(arr, smallest)
    }
}

exports.siftMaxDown = function siftMaxDown(array, start, end) {
    let root = start
    let left = (2 * root) + 1
    while(left <= end) {
        let swap = root
        if(array[swap] < array[left]) {
            swap = left
        } 
        if((left+1) <= end && array[swap] < array[left+1]) {
            swap = left+1
        }
        if(swap == root) {
            return
        }
        module.exports.swap(root, swap, array)
        root = swap
        left = (2 * root) + 1
    }
}

exports.siftMinDown = function siftMinDown(array, start, end) {
    let root = start
    let left = (2 * root) + 1
    while(left <= end) {
        let swap = root
        if(array[swap] > array[left]) {
            swap = left
        } 
        if((left+1) <= end && array[swap] > array[left+1]) {
            swap = left+1
        }
        if(swap == root) {
            return
        }
        module.exports.swap(root, swap, array)
        root = swap
        left = (2 * root) + 1
    }
}

exports.buildMaxHeap = function buildMaxHeap(arr) {
    for(let i = Math.floor(arr.length / 2); i >= 0; i--) {
        module.exports.maxHeapify(arr, i)
    }
}

exports.buildMinHeap = function buildMinHeap(arr) {
    for(let i = Math.floor(arr.length / 2); i >= 0; i--) {
        module.exports.minHeapify(arr, i)
    }
}

exports.binarySearch = function binarySearch(target, array) {
    let mid = Math.floor(array.length / 2)
    let low = 0
    let high = array.length - 1
    while(low <= high) {
        if(array[mid] == target) {
            return [mid, target, true]
        }
        console.log(array[mid])
        if(array[mid] > target) {
            high = mid - 1
        } else if(array[mid] < target) {
            low = mid + 1
        }
        mid = Math.floor((high + low) / 2)
    }
    return [-1, false]
}

exports.partition = function partition(array, low, high) {
    let pivot = array[Math.floor((low + high) / 2)]
    let i = low
    let j = high
    while(true) {
        while (array[i] < pivot) {
            i++
        }
        while (array[j] > pivot) {
            j--
        }
        if(i >= j) {
            return j
        }
        module.exports.swap(i, j, array)
    }
}

exports.directedGraphGen = function directedGraphGen(nodeArray, maxEdge) {
    let adjacency = {}
    let copy = [...nodeArray]
    for(let node of nodeArray) {
        adjacency[node] = []
    }
    module.exports.shuffle(copy)
    for(let node of Object.keys(adjacency)) {
        let edges = Math.floor(Math.random() * (maxEdge - 1)) + 1
        while(edges > 0) {
            let popped = copy.pop()
            if(!popped) {
                break
            }
            adjacency[node].push(popped)
            edges--
        }
    }
    return adjacency
}

exports.undirectedGraphGen = function undirectedGraphGen(nodeArray, maxEdge) {
    let adjacency = {}
    let copy = [...nodeArray]
    for(let node of nodeArray) {
        adjacency[node] = []
    }
    module.exports.shuffle(copy)
    for(let node of Object.keys(adjacency)) {
        let edges = Math.floor(Math.random() * (maxEdge - 1)) + 1
        while(edges > 0) {
            let popped = copy.pop()
            if(!popped) {
                break
            }
            adjacency[node].push(popped)
            adjacency[popped].push(node)
            edges--
        }
    }
    return adjacency
}
