/**
 * @param {Function} fn
 */
function memoize(fn) {
    let memo = {}
    return function(...args) {
        if(memo[`${args}`] !== undefined) {
            return memo[`${args}`]
        }
        memo[`${args}`] = fn(...args)
        return memo[`${args}`]
    }
}
