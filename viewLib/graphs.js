const { matrixGen } = require('./utils.js')

function islandsGen(gridSize) {
    let matrix = matrixGen(gridSize, gridSize, 0)
    for(let row of matrix) {
        for(let i = 0; i < row.length; i++) {
            let rand = Math.random()
            if(rand >= 0.5) {
                row[i] = 1;
            }
        }
    }
    return matrix
}

function checkConnectingNeighbors(indexPair, matrix) {
    let [ i, j ] = indexPair
    if(!matrix[i] || !matrix[i][j]) {
        return false
    }
    if(matrix[i][j] == 1) {
        matrix[i][j] = 0
        checkConnectingNeighbors([i+1, j], matrix)
        checkConnectingNeighbors([i, j+1], matrix)
        checkConnectingNeighbors([i-1, j], matrix)
        checkConnectingNeighbors([i, j-1], matrix)
        return true
    }
    return false
}

function countIslands(islandMatrix) {
    let num = 0
    for(let i = 0; i < islandMatrix.length; i++) {
        for(let j = 0; j < islandMatrix[0].length; j++) {
            if(checkConnectingNeighbors([i,j], islandMatrix)) {
               num++ 
            }
        } 
    }
    return num
}

module.exports = { islandsGen, countIslands }
