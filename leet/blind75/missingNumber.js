function missingNumber(nums) {
  let max = nums.length + 1
  let sum = (max / 2) * (max - 1)
  for(let num of nums) {
    sum -= num
  }
  return sum
}

function missingNumberBits(nums) {
  let res = nums.pop()
  for(let num of nums) {
    res = res ^ num
  }
  for(let i = 0; i <= nums.length+1; i++) {
    res = res ^ i
  }
  return res
}

console.log(missingNumberBits([9,6,4,2,3,5,7,0,1]))
