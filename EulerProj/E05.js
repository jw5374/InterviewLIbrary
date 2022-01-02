const { arrayGen } = require("../viewLib/utils.js")

// function factorial(n) {
//     if(n <= 1) {
//         return 1
//     }
//     return n * factorial(n-1)
// }

function extractModulus(array) {
    let compressed = []
    for(let i = array.length - 1; i >= 0; i--) {
        for(let j = i-1; j >= 0; j--) {
            if(array[j] && (array[i] % array[j] == 0)) {
                array[j] = false
            }
        }
    }
    for(let num of array) {
        if(num) {
            compressed.push(num)
        }
    }
    return compressed
}

function multAll(array) {
    let res = 1
    for(let num of array) {
        res *= num
    }
    return res
}

let array1 = arrayGen(21)
array1.shift()

let attempt = extractModulus(array1)
console.log(((multAll(attempt) / 12) / 12) / 20) // 232792560 no idea how it works
