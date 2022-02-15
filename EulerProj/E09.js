function generateTriple(n, m) {
    let b = ( m ** 2 - n ** 2 ) / 2
    let a = (m * n)
    let c = ( m ** 2 + n ** 2 ) / 2
    return [a, b, c]
}

function sumTriple(triple) {
    let sum = 0
    for(let num of triple) {
        sum += num
    }
    return sum
}

function naiveSolution() {
    let sum = 0
    let triple
    for(let n = 1; n < 100; n+=2) {
        for(let m = n+2; m < 105; m+=2) {
            triple = generateTriple(n, m)
            console.log(triple)
            sum = sumTriple(triple)
            if(sum == 1000) {
                return [sum, triple]
            }
        }
    }
}

console.log(naiveSolution()) // [ 1000, [ 375, 200, 425 ] ] product = 31,875,000
