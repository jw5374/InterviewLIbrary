// doesn't work
function removeDuplicates(s) {
  let split = s.split("")
  let i = 0
  for(let i = 0; i < split.length; i++) {
    let j = i
    let k = i+1
    while(split[j] == split[k]) {
      split.splice(j, 2)
    }
  }
  return split.join("")
}

// too slow
function slowRemove(s) {
  let split = s.split("")
  let i = 0
  for(let i = 0; i < split.length; i++) {
      let j = i
      let k = i+1
      while(j >= 0 && k < split.length) {
          while(split[j] == "") {
              j--
          }
          while(split[k] == "") {
              k++
          }
          if(split[j] == split[k]) {
              split[j] = ""
              split[k] = ""
              j--
              k++
          } else {
              break
          }
      }
  }
  return split.join("")
}


console.log(slowRemove("ibfjcaffccadidiaidchakchchcahabhibdcejkdkfbaeeaecdjhajbkfebebfea"))
