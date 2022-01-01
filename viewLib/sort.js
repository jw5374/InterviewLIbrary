const { swap, mergeSorted } = require("./utils.js")

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
    
}

function quickSort(array) {
    
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

module.exports = { insertionSort, selectionSort, shellSort, mergeSort, heapSort, quickSort, bubbleSort }