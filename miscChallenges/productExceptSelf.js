function productExceptSelf(nums) {
  let pre = [nums[0]]
  let post = [nums[nums.length-1]]
  let answer = []
  for(let i = 1; i < nums.length; i++) {
    pre.push(nums[i] * pre[i-1])
  }
  for(let i = nums.length-2; i >= 0; i--) {
    post.unshift(nums[i] * post[0])
  }
  for(let i = 0; i < nums.length; i++) {
    if(i == 0) {
      answer.push(post[i+1])
      continue
    }
    if(i == nums.length - 1) {
      answer.push(pre[i-1])
      continue
    }
    answer.push(pre[i-1] * post[i+1]) 
  } 
  return answer
}

let result = productExceptSelf([-1,1,0,-3,3])
console.log(result)
