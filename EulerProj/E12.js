const { sumOfFirstNatural } = require("./E06.js")

function findNaturalFactors(num) {
    // let factors = []
    let numFactors = 0 // might be faster since we don't care what the factors are
    for(let i = 1; i < Math.floor(Math.sqrt(num)); i++) {
        if(num % i == 0) {
            if(num / i == 1) {
                // factors.push(i)
                numFactors++
            } else {
                // factors.push(i)
                // factors.push(num/i)
                numFactors+=2
            }
        }
    }
    return numFactors
}

let factorNum = 0;
let num = 8
let triNum;
while(factorNum <= 500) {
    triNum = sumOfFirstNatural(num++)
    factorNum = findNaturalFactors(triNum)
}

console.log(triNum, num, factorNum)

module.exports = { findNaturalFactors }
