function countMultiples(num, x) {
    return Math.floor(num/x)
}

function findMultipleSum(num, x) {
    let mults = countMultiples(num, x)
    let sum = 0
    for(let i = 1; i <= mults; i++) {
        sum += i*x
    }
    return sum
}


function naiveAttempt(num) {
    let sum = 0
    for(let i = 1; i < num; i++) {
        if(i % 3 == 0 || i % 5 == 0) {
            sum += i
        }
    }
    return sum
}

// let result = findMultipleSum(999, 3) + findMultipleSum(999, 5) - findMultipleSum(999, 15)
// console.log(result)
// console.log(naiveAttempt(1000))

module.exports = { findMultipleSum, countMultiples }