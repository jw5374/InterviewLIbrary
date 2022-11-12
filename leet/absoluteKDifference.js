// doesn't work
function countKDifference(nums, k) {
  let dict = {}
  let res = 0
  for(let num of nums) {
    if(dict[num] != undefined) {
      dict[num]++
    } else {
      dict[num] = 1
    }
  }
  for(let num of nums) {
    let diff = Math.abs(k >= num ? k+num : k-num)
    console.log(dict)
    if(dict[diff] != undefined && dict[num] > 0) {
      res++
      dict[diff]--
    }
  }
  return res
}

// naive slow
function slowKDifference(nums, k) {
  let res = 0
  for(let i = 0; i < nums.length; i++) {
    for(let j = i+1; j < nums.length; j++) {
      if(Math.abs((nums[i] - nums[j])) == k) {
        res++
      }
    }
  }
  return res
}

console.log(slowKDifference([3,2,1,5,4], 10))
