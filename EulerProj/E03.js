// arrays of numbers [1...n]
function sieveOfEratosthenes(rangeArray) {
    for(let i = 1; i < Math.pow(rangeArray.length, 0.5); i++) {
        if(rangeArray[i]) {
            for(let j = rangeArray[i] * rangeArray[i] - 1; j < rangeArray.length; j+=rangeArray[i]) {        
                rangeArray[j] = false
            }
        }
    }
}

function extractSieve(array) {
    let primes = []
    for(let num of array) {
        if(num) {
            primes.push(num)
        }
    }
    return primes
}

function factorizeNaive(num, primes) {
    if(num <= 3) {
        return num
    }
    let factors = []
    for(let prime of primes) {
        if(num == 1) {
            return factors
        }
        if(num % prime == 0) {
            num /= prime
            factors.push(prime)
        }
    }
}

// let sequence = [...Array(100000000).keys()]
// sieveOfEratosthenes(sequence)
// let primes = extractSieve(sequence)
// primes.splice(0, 1)
// let factors = factorizeNaive(600851475143, primes)

module.exports = { sieveOfEratosthenes, extractSieve }