// doesn't work
function rotate(nums, k) {
  let rem = k % nums.length
  if(nums.length <= 1 || rem == 0) {
    return
  }
  let [i,j] = [0, k]
  while(j < nums.length) {
    let temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    i++
    j++
  }
  return nums
}

// shifting and pushing
function popRotate(nums, k) {
  let i = 0
  while(i < k % nums.length) {
    nums.push(nums.shift())
    i++
  }
  return nums
}

// console.log(rotate([1,2,3,4,5,6,7], 3))
console.log(popRotate([1,2,3,4,5,6,7], 10))
