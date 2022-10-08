/*
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
*/

function maxArea(height) {
  let [left, right] = [0, height.length-1]
  let max = 0
  while(left < right) {
    let contHeight = Math.min(height[left], height[right])
    let contWidth = right - left
    let area = contHeight * contWidth
    if(area > max) {
      max = area
    }
    if(height[left] < height[right]) {
      left++
    } else {
      right--
    }
  }
  return max
}

console.log(maxArea([1,8,6,2,5,4,8,3,7]))
