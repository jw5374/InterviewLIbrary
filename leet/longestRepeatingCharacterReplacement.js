// unsolved
function characterReplacement(s, k) {
  let freqMap = {}
  let [left, right] = [0, 0]
  let split = s.split("")
  let maxChar = 0
  let max = 0
  while(right < split.length) {
    let windowLength = (right - left) + 1
    if(freqMap[split[right]] != undefined) {
      freqMap[split[right]]++
    } else {
      freqMap[split[right]] = 1
    }
    maxChar = Math.max(maxChar, freqMap[split[right]])
    if(windowLength - maxChar <= k) {
      max = Math.max(max, windowLength)
      right++
      continue
    }
    while(windowLength - maxChar > k) {
      freqMap[split[left]]--
      left++
      windowLength = (right - left) + 1
    }
    right++
  }
  return max
}

console.log(characterReplacement("ABABBA", 2))
