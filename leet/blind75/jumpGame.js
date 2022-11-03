// very slow, probably not memoizing properly
function canJump(nums) {
  if(nums.length == 1) {
    return true
  }
  return depth(nums)
}

function depth(nums, i = 0, memo = {}) {
  if(memo[i] != undefined) {
    return memo[i]
  }
  if(i >= nums.length-1) {
    return true
  }
  if(nums[i] == 0) {
    return false
  }
  for(let j = i+1; j <= i + nums[i]; j++) {
    if(depth(nums, j, memo)) {
      return true
    }
    memo[j] = false
  }
  return false
}

console.log(canJump([2,0,0])) // [2,3,1,1,4]
