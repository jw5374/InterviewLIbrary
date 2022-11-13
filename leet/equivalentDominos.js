function numEquivDominoPairs(dominoes) {
  let hash = {}
  let res = 0
  for(let domino of dominoes) {
    if(hash[`${domino[0]},${domino[1]}`] != undefined) {
      hash[`${domino[0]},${domino[1]}`]++
    } else if(hash[`${domino[1]},${domino[0]}`] != undefined) {
      hash[`${domino[1]},${domino[0]}`]++
    } else {
      hash[`${domino[0]},${domino[1]}`] = 1
    }
  }
  for(let key in hash) {
    if(hash[key] > 1) {
      res += (hash[key] * (hash[key] - 1)) / 2
    }
  }
  return res 
}

console.log(numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]))
