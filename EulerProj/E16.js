let bigPower = BigInt(2 ** 1000)

let normalSum = 0
for(let digit of bigPower.toString().split("")) {
    normalSum += parseInt(digit)
}

let stringNum =  bigPower.toString()
let charAtSum = 0
for(let i = 0; i < stringNum.length; i++) {
    charAtSum += parseInt(stringNum.charAt(i))
}

let sum = 0n
while(bigPower > 0n) {
    let digit = bigPower % 10n
    sum += digit
    bigPower /= 10n
}

console.log(sum, normalSum, charAtSum)
