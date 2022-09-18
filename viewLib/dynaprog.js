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

//unsolved
exports.coinChange = function coinChange(coins, amount, memo = {0: 0}, min = amount+1) {
    coins.sort((a, b) => b - a)
    if(amount in memo) {
        return memo[amount]
    }
    for(let i = 0; i < coins.length; i++) {
        let remaining = amount - coins[i]
        if(remaining < 0) {
            continue
        }
        if(remaining >= 0) {
            memo[amount] = Math.min(amount + 1, 1 + coinChange(coins, remaining, memo, min))
            if(min > memo[amount]) {
                min = memo[amount]
            }
        }
    }
    if(min != amount+1) {
        return min
    }
    return -1
}

exports.coinChangeIter = function coinChangeIter(coins, amount) {
    let memo = []
    for(let i = 0; i < amount+1; i++) {
        memo.push(amount+1)
    }
    memo[0] = 0;
    for(let i = 1; i < amount+1; i++) {
        for(let coin of coins) {
            if((i - coin) >= 0) {
                memo[i] = Math.min(memo[i], 1 + memo[i - coin])
            }
        }
    }
    if(memo[amount] != amount+1) {
        return memo[amount]
    }
    return -1
}
