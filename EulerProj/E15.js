const { matrixGen } = require("../viewLib/utils.js")

let lattice = matrixGen(21, 21)

lattice[20][20] = 1

let memo = {}

function traverseLatticeDownRight(i, j, latt) {
    let sum = 0
    if(`${i},${j}` in memo) {
        return memo[`${i},${j}`]
    }
    if(i >= latt.length) {
        return 0
    }
    if(j >= latt[0].length) {
        return 0
    }
    if(latt[i][j] == 1) {
        return 1
    }
    memo[`${i},${j+1}`] = sum + traverseLatticeDownRight(i, j+1, latt)
    memo[`${i+1},${j}`] = sum + traverseLatticeDownRight(i+1, j, latt)
    return memo[`${i},${j+1}`] + memo[`${i+1},${j}`]
}

let ways = traverseLatticeDownRight(0, 0, lattice)
console.log(ways)
