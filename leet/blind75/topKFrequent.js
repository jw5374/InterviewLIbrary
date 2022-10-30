function topKFrequent(nums, k) {
  let freqs = catCounter(nums) 
  let freqArr = Array.from(Array(nums.length+1))
  let top = []
  for(let [key, value] of Object.entries(freqs)) {
    if(freqArr[value] != undefined) {
      freqArr[value].push(key)
    } else {
      freqArr[value] = [key]
    }
  }
  for(let i = freqArr.length-1; i >= 0; i--) {
    if(freqArr[i] != undefined) {
      for(let num of freqArr[i]) {
        if(top.length < k) {
          top.push(num)
        } else {
          break
        }
      }
    }
    if(top.length == k) {
      break
    }
  }
  return top
}

function catCounter(arr, cats = {}) {
  for(let num of arr) {
    if(cats[num] != undefined) {
      cats[num]++
    } else {
      cats[num] = 1
    }
  }
  return cats
}


console.log(topKFrequent([1,1,1,2,2,3,3,5,3,2,4,4,6,7,3,9,56,2,2,3,4], 4))
