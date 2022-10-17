// See Euler problem 15 and dynaprog.js (gridTrav) 
// Same problem, repeated solutions
function uniquePaths(m, n, memo = {}) {
    let key = `${m},${n}`
    let altkey = `${n},${m}`
    if(key in memo) {
        return memo[key]
    }
    if(m == 1 || n == 1) {
        return 1
    }
    if(m == 0 || n == 0) {
        return 0
    }
    let returnVal = uniquePaths(m - 1, n, memo) + uniquePaths(m, n - 1, memo)
    memo[key] = returnVal
    memo[altkey] = returnVal
    return returnVal
}

console.log(uniquePaths(3, 7))
