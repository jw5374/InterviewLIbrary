function lengthOfLongestSubstring(s) {
  if(s.length == 1) {
    return 1
  }
  let [left, right] = [0, 1]
  let split = s.split("")
  let max = 0
  while(right < split.length) {
    let slice = split.slice(left, right+1)
    let set = new Set(slice)
    if(set.size == slice.length) {
      if(set.size > max) {
        max = set.size
      }
      right++
    } else {
      if(left < right) {
        left++
      } else {
        right++
      }
    }
  }
  return max
}

console.log(lengthOfLongestSubstring("abc12d^&4"))
