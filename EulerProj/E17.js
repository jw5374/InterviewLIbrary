// NUMBER LETTERS (1-1000)
let conversionTable = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


// naive conversion strategy
function convertNumbersToLetters(num) {
    if(num in conversionTable) {
        return conversionTable[num]
    }
    let stringNum = num.toString()
    let numSplit = stringNum.split("").map((el) => parseInt(el))
    switch(stringNum.length) {
        case 2:
            return `${conversionTable[numSplit[0] * 10]}${conversionTable[numSplit[1]]}`
        case 3:
            return `${conversionTable[numSplit[0]]}hundred${(numSplit[1] == 0 && numSplit[2] == 0) ? "" : "and"}${numSplit[1] == 1 ? conversionTable[(numSplit[1] * 10) + numSplit[2]] : conversionTable[numSplit[1] * 10] + conversionTable[numSplit[2]]}`
        case 4:
            return `${conversionTable[1]}thousand`
    }
}

let sumofletters = 0

for(let i = 1; i <= 1000; i++) {
    sumofletters += convertNumbersToLetters(i).length
}

console.log(sumofletters)