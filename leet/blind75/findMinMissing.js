/*
Input: nums = [1,2,0]
Output: 3

Input: nums = [3,4,-1,1]
Output: 2

Input: nums = [7,8,9,11,12]
Output: 1
*/
function firstMissingPositive(nums) {
  for(let i = 0; i < nums.length; i++) {
    if(nums[i] < 0) {
      nums[i] = 0
    }
  }
  for(let i = 0; i < nums.length; i++) {
    let num = Math.abs(nums[i])
    if(nums[num-1] != undefined && nums[num-1] > 0) {
      nums[num-1] *= -1
    }
  }
  for(let i = 1; i <= nums.length+1; i++) {
    if(nums[i-1] != undefined && nums[i-1] >= 0) {
      return i
    }
  }
}

console.log(firstMissingPositive([1,2,0]))
