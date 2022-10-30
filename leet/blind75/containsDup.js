function containsDuplicate(nums) {
  let res = new Set(nums)
  if(res.size == nums.length) {
    return false
  }
  return true
}


console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
console.log(containsDuplicate([1,2,3,4]))
console.log(containsDuplicate([1,2,3,1]))
