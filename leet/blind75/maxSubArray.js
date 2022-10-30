/*
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
*/

// sum of max subarray
function maxSubArray(nums) {
  let sub = nums[0]
  let global = nums[0]
  for(let i = 1; i < nums.length; i++) {
    sub = Math.max(nums[i], sub + nums[i]) // either consider just the next element, or both elements combined
    if(global < sub) { // if global max is less then consider new current max
      global = sub
    }
  }
  return global
}

function maxSubVals(nums) {
  let sub = nums[0]
  let global = nums[0]
  let left = 0
  let right = 0
  for(let i = 1; i < nums.length; i++) {
    if(sub+nums[i] < nums[i]) {
      left = i
    }
    sub = Math.max(nums[i], sub + nums[i])
    if(global < sub) {
      global = sub
      right = i
    }
  }
  return nums.slice(left, right+1)
}

console.log(maxSubVals([-2,1,-3,4,-1,2,1,-5,4]))
