
// naive solution
function sumBase(n, k) {
  let numBase = n.toString(k)
  let result = 0
  for(let i = 0; i < numBase.length; i++) {
    result += parseInt(numBase.charAt(i))
  }
  return result
}

console.log(sumBase(10, 10))
