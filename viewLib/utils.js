exports.arrayGen = function arrayGen(n) {
    return [...Array(n).keys()]
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
