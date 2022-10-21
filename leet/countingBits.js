// return array of size n+1 where each element ans[i] = the number of one bits in i

function countBits(n) {
  let ans = []
  for(let i = 0; i <= n; i++) {
    ans.push(hammingBits(i))
  }
  return ans
}

// oneBits problem
function hammingBits(n) {
  let numBit = 0
  let pow = 0
  while(n != 0) {
    n = n&(n-1)
    numBit++
  }
  return numBit
}

console.log(countBits(10**5))
