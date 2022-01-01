function genFibLessThan(n) {
    let fibnums = [1, 1]
    let count = 0;
    let seq = []
    seq.push(fibnums[0])
    seq.push(fibnums[1])
    while(count < n) {
        count = fibnums[0] + fibnums[1]
        seq.push(count)
        fibnums[0] = fibnums[1]
        fibnums[1] = count
    }
    return seq
}

function sumFibSeqMultiple(fibArray, x) {
    fibArray.pop()
    let sum = 0
    for(let num of fibArray) {
        if(num % x == 0) {
            sum += num
        }
    }
    return sum
}

// let fibBelow = genFibLessThan(4000000)
// console.log(sumFibSeqMultiple(fibBelow, 2))