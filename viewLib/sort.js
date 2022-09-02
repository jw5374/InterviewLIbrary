const { swap, mergeSorted, partition, buildMaxHeap, siftMaxDown } = require("./utils.js")

function insertionSort(array) {
    for(let i = 0; i < array.length; i++) {
        let itemIndex = i
        while(array[itemIndex - 1] && array[itemIndex - 1] > array[itemIndex]) {
            swap(itemIndex, itemIndex-1, array)
            itemIndex--
        }
    }
    return array
}

function insertionSortIndex(array, low, high) {
    for(let i = low; i < high; i++) {
        let itemIndex = i+1
        while(itemIndex > low && array[itemIndex - 1] && array[itemIndex - 1] > array[itemIndex]) {
            swap(itemIndex, itemIndex-1, array)
            itemIndex--
        }
    }
    return array
}

function selectionSort(array) {
    let currMin
    for(let i = 0; i < array.length; i++) {
        currMin = i
        for(let j = i+1; j < array.length; j++) {
            if(array[currMin] > array[j]) {
                currMin = j
            }
        }
        swap(i, currMin, array)
    }
    return array
}

function selectionSortIndex(array, low, high) {
    let currMin
    for(let i = low; i < high; i++) {
        currMin = i
        for(let j = i+1; j < high; j++) {
            if(array[currMin] > array[j]) {
                currMin = j
            }
        }
        swap(i, currMin, array)
    }
    return array
}

function shellSort(array) {
    
}

function mergeSort(array) {
    if(array.length <= 7) {
        return insertionSort(array)
    }
    let mid = Math.floor(array.length / 2)
    let arraySplit = [array.slice(0, mid), array.slice(mid)]
    let array1 = mergeSort(arraySplit[0])
    let array2 = mergeSort(arraySplit[1])
    return mergeSorted(array1, array2)
}

function heapSort(array) {
    let last = array.length - 1
    buildMaxHeap(array)
    while(last > 0) {
        swap(0, last, array)
        last--
        siftMaxDown(array, 0, last)
    }
    return array
}

function quickSort(array, low, high) {
    let size = high - low
    if(size <= 9) {
        insertionSortIndex(array, low, high)
    } else if(low >= 0 && high >= 0 && low < high) {
        let pivot = partition(array, low, high)
        quickSort(array, low, pivot)
        quickSort(array, pivot+1, high)
    }
}

function bubbleSort(array) {
    let unsorted
    while(true) {
        unsorted = 0
        for(let i = 0; i < array.length; i++) {
            if(array[i] > array[i + 1]) {
                swap(i, i+1, array)
                unsorted++
            }
        }
        if(!unsorted) {
            break // return array
        }
    }
}

function bubbleSortIndex(array, low, high) {
    let unsorted
    while(true) {
        unsorted = 0
        for(let i = low; i < high; i++) {
            if(array[i] > array[i + 1]) {
                swap(i, i+1, array)
                unsorted++
            }
        }
        if(!unsorted) {
            break // return array
        }
    }
}

module.exports = { insertionSort, selectionSort, shellSort, mergeSort, heapSort, quickSort, bubbleSort }