function checkPalindrome(num) {
    let half = 0
    let numCopy = num
    while(numCopy > 0) {
        half *= 10
        half += numCopy % 10
        numCopy = Math.floor(numCopy / 10)
    }
    if(num == half) {
        return true
    }
    return false
}


function naiveSolution() {
    let palindromes = []
    for(let i = 999; i >= 100; i--) {
        for(let j = 999; j >= 100; j--) {
            let product = i*j
            if(checkPalindrome(product)) {
                palindromes.push(product)
            }
        }
    }
    return palindromes.sort((a,b) => b - a)[0]
}

// console.log(naiveSolution())