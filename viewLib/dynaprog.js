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
    let results = []
    for(let i = 0; i < array.length; i++) {
        let sum = target - array[i]
        memo[sum] = canSum(sum, array, memo)
        results.push(memo[sum])
    }
    for(let res of results) {
        if(res) {
            return true
        }
    }
    return false
}

exports.canSumLimited = function canSum(target, array, memo = {}) {
    if(target in memo) {
        return memo[target]
    }
    if(target == 0) {
        return true
    }
    if(target < 0) {
        return false
    }
    let results = []
    for(let i = 0; i < array.length; i++) {
        let sum = target - array[i]
        let sliced = array.slice(0, i).concat(array.slice(i+1))
        memo[sum] = canSum(sum, sliced, memo)
        results.push(memo[sum])
    }
    for(let res of results) {
        if(res) {
            return true
        }
    }
    return false
}

exports.findWays = function findWays(n, memo = {}) {
    if(n in memo) {
        return memo[n]
    }
    if(n <= 0) {
        return 0
    }
    if(n == 1) {
        return 1
    }
    if(n == 2) {
        return 2
    }
    memo[n] = findWays(n-2, memo) + findWays(n-1, memo) 
    return memo[n]
}