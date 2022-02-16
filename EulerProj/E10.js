const { sieveOfEratosthenes, extractSieve } = require('./E03.js')
const { arrayGen } = require('../viewLib/utils.js')
let numArray = arrayGen(2000000)
sieveOfEratosthenes(numArray)
let primesBelow = extractSieve(numArray)

function sumArray(array) {
    let sum = 0
    for(let num of array) {
        sum += num
    }
    return sum
}

console.log(primesBelow)
console.log(sumArray(primesBelow) - 1) // primes array has 1 which is not included thus need to subtract

