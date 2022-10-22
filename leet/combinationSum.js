function combinationSum(candidates, target) {
  let results = []
  dfs(0, target, candidates, 0, results)
  return results
}

function dfs(index, target, candidates, total, resultsArr, localCombo = []) {
  if(target == total) {
    resultsArr.push([...localCombo])
    return
  }
  if(index >= candidates.length || total > target) {
    return
  }
  localCombo.push(candidates[index])
  dfs(index, target, candidates, total + candidates[index], resultsArr, localCombo)
  localCombo.pop()
  dfs(index + 1, target, candidates, total, resultsArr, localCombo)
}

console.log(combinationSum([2], 1))
