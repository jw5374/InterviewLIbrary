function longestCommonPrefix(strs) {
    strs = strs.sort((a, b) => a.length - b.length)
    let checker = strs.shift()
    let i = checker.length - 1
    for(let word of strs) {
        while(!word.startsWith(checker)) {
            checker = checker.substring(0, i--)
        }
    }
    return checker
} 

console.log(longestCommonPrefix(["flower","flow","flight"]))
