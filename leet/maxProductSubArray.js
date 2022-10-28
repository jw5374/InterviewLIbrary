function maxProduct(nums) {
  let res = Math.max(...nums)
  let [localMin, localMax] = [1, 1]
  for(let num of nums) {
    let tmpMax = localMax * num
    localMax = Math.max(num * localMax, num * localMin, num)
    localMin = Math.min(tmpMax, num * localMin, num)
    res = Math.max(res, localMax, localMin)
  }
  return res
}

console.log(maxProduct([2,3,-2,0,4]))
