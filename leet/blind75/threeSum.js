function threeSum(nums) {
  nums.sort((a,b) => a - b)
  if(nums.length == 3) {
    let sum = nums.reduce((a,b) => a + b)
    return sum == 0 ? [nums] : []
  }
  let results = []
  for(let i = 0; i < nums.length-2; i++) {
    let pairs = twoSum(i+1, nums.length, nums, (nums[i] == 0 ? 0 : nums[i] * -1))
    for(let pair of pairs) {
      results.push([nums[i], pair[0], pair[1]])
    }
  }
  let dupDict = {}
  for(let i = 0; i < results.length; i++) {
    if(dupDict[results[i].toString()] != undefined) {
      results.splice(i, 1)
      i--
    } else {
      dupDict[results[i].toString()] = 1
    }
  }
  return results
}

function twoSum(start, end, nums, target) {
  let results = []
  let visited = {}
  let dictLocal = {}
  for(let i = start; i < end; i++) {
      if(dictLocal[nums[i]] != undefined) {
          dictLocal[nums[i]].push(i)
      } else {
          dictLocal[nums[i]] = [i]
      }
  }
  for(let i = start; i < end; i++) {
      let remaining = target - nums[i]
      if(dictLocal[remaining] != undefined && visited[remaining] == undefined && (dictLocal[remaining].length > 1 || remaining != nums[i])) {
          results.push([nums[i], nums[dictLocal[remaining].pop()]])
          visited[nums[i]] = 1
          visited[remaining] = 1
      }
  }
  return results
}


console.log(threeSum([-1,0,1,2,-1,-4]))


// need to use indexes to increase speed and decrease memory
