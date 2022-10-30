function isPalindrome(s) {
    let chars = s.toLowerCase().match(/([a-z0-9])/g)
    if(!chars) {
        return true
    }
    let i = 0
    let j = chars.length - 1
    while(i < j) {
        if(chars[i] != chars[j]) {
            return false
        }
        i++
        j--
    }
    return true
}

console.log(isPalindrome("A man, a plan, a canal: Panama"))
