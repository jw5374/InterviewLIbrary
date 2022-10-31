function rotatedSearch(nums, target) {
  let [low, high] = [0, nums.length-1]
  while(low <= high) {
    let mid = Math.floor((low + high) / 2)
    if(nums[mid] == target) {
      return mid
    }
    if(nums[mid] >= nums[low]) {
      if(nums[mid] < target) {
        low = mid + 1
        continue
      } 
      if(nums[low] > target) {
        low = mid + 1
      } else {
        high = mid - 1
      }
    } else {
      if(nums[mid] > target) {
        high = mid - 1
        continue
      }
      if(nums[high] < target) {
        high = mid - 1
      } else {
        low = mid + 1
      }
    }
  }
  return -1
}

console.log(rotatedSearch([4,5,6,7,0,1,2], 0))
