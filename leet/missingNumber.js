function missingNumber(nums) {
  let max = nums.length + 1
  let sum = (max / 2) * (max - 1)
  for(let num of nums) {
    sum -= num
  }
  return sum
}

console.log(missingNumber([9,6,4,2,3,5,7,0,1]))
