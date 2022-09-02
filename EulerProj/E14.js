/*
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
*/

function collatzGenerator(startNum) {
    let sequence = [startNum]
    while(startNum > 1) {
        if(startNum % 2 == 0) {
            startNum /= 2
        } else {
            startNum = (3 * startNum) + 1
        }
        sequence.push(startNum)
    }
    return sequence
}

let currLongest = [0, 0]

for(let i = 14; i < 1000000; i++) {
    let localSequenceLength = collatzGenerator(i).length
    if(localSequenceLength > currLongest[0]) {
        currLongest[0] = localSequenceLength
        currLongest[1] = i
    }
}

console.log(currLongest)
