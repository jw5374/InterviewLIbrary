function sumOfFirstNatural(n) {
    let sum = (n * (n + 1)) / 2 // sum of arithmetic progression
    return sum
}

function sumOfFirstSquares(n) {
    let sum = (n * (n + 1) * ((2*n) + 1)) / 6 // sum of first squares
    return sum
}

// let answer = Math.pow(sumOfFirstNatural(100), 2) - sumOfFirstSquares(100)
// console.log(answer)
