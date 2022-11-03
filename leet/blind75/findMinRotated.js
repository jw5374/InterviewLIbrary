function findMin(nums) {
  let [left, right] = [0, nums.length-1]
  while(left <= right) {
    let mid = Math.floor((left + right) / 2)
    if(nums[left] <= nums[right]) {
      return nums[left]
    } else {
      if(nums[mid-1] > nums[mid]) {
        return nums[mid]
      }
      if(nums[left] <= nums[mid]) {
        left = mid + 1
      } else {
        right = mid - 1
      }
    }
  }
}

console.log(findMin([3,1,2]))
