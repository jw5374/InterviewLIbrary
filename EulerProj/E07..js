const { sieveOfEratosthenes, extractSieve } = require("./E03.js")
const { arrayGen } = require("../viewLib/utils.js")

function primeGen(n, i = 1) {
    let array = arrayGen(n)
    sieveOfEratosthenes(array)
    let extract = extractSieve(array)
    while(extract.length < n) {
        array.push(n + (i++))
        sieveOfEratosthenes(array)
        if(array[array.length - 1]) {
            extract.push(array[array.length - 1])
        }
    }
    return extract
}

// let primes = primeGen(10002)
// console.log(primes.slice(-1))