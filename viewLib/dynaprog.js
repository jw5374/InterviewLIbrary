exports.fibGen = function fibGen(n, memo = {}, seqArry = []) {
    if(n in memo) {
        return memo[n]
    }
    if(n <= 2) {
        return 1
    }
    memo[n] = fibGen(n-1, memo) + fibGen(n-2, memo)
    seqArry.push(memo[n])
    return memo[n]
}

exports.gridTrav = function gridTrav(rows, cols, memo = {}) {
    let key = `${rows}, ${cols}`
    let altKey = `${cols}, ${rows}`
    if(key in memo) {
        return memo[key]
    }
    if(rows == 1 || cols == 1) {
        return 1
    }
    if(rows == 0 || cols == 0) {
        return 0
    }
    let retVal = gridTrav(rows - 1, cols, memo) + gridTrav(rows, cols - 1, memo)
    memo[key] = retVal
    memo[altKey] = retVal
    return retVal
}

exports.canSum = function canSum(target, array, memo = {}) {
    if(target in memo) {
        return memo[target]
    }
    if(target == 0) {
        return true
    }
    if(target < 0) {
        return false
    }
    for(let i = 0; i < array.length; i++) {
        let sum = target - array[i]
        memo[sum] = canSum(sum, array, memo)
    }
    
}
