// string manipulation
function hammingWeight(n) {
    let numBits = 0
    for(let bit of n.toString(2)) {
        if(bit == '1') {
            numBits++
        }
    }
    return numBits
}

// bit manip version
function hammingBits(n) {
  let numBit = 0
  let pow = 0
  while(n != 0) {
    n = n&(n-1)
    numBit++
  }
  return numBit
}

console.log(hammingArithmetic(5))
