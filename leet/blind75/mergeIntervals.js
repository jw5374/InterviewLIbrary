function merge(intervals) {
  if(intervals.length <= 1) {
    return intervals
  }
  intervals.sort((a,b) => a[0] - b[0])
  let result = []
  for(let i = 0; i < intervals.length; i++) {
    let initial = intervals[i]
    if(initial == -1) {
      continue
    }
    let j = i+1
    while(j < intervals.length && initial[1] >= intervals[j][0]) {
      if(initial[1] <= intervals[j][1]) {
        initial[1] = intervals[j][1]
      }
      intervals[j] = -1
      j++
    }
    result.push(initial)
  }
  return result
}

console.log(merge([[1,3],[2,6],[8,10],[15,18]]))
