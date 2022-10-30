// only string version works with leetcode
function reverseBitsString(n) {
  let string = ""
  for(let i = 0; i < 32; i++) {
    let digit = (n >> i) & 1
    string += digit
  }
  return parseInt(string, 2)
}

// returning signed values, but should still be properly reversing bits, not accepted by leetcode
function reverseBits(n) {
  let res = 0
  for(let i = 0; i < 32; i++) {
    let digit = (n >> i) & 1
    res = res | (digit << (31 - i))
  }
  return res
}

console.log(reverseBits(4294967293))
