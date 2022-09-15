function transpose(matrix) {
    for(let i = 0; i < matrix.length; i++) {
        for(let j = i; j < matrix[0].length; j++) {
            let temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        }
    }
    return matrix
}

function checkNeighbors(matrix, indexpair) {
    let [i, j] = indexpair
    let neighborcells = []
    if(matrix[i+1] != undefined) {
        neighborcells.push([i+1, j])
    }
    if(matrix[i-1] != undefined) {
        neighborcells.push([i-1, j])
    }
    neighborcells.push([i, j+1])
    neighborcells.push([i, j-1])
    let same = 0
    for(let neighbor of neighborcells) {
        if(matrix[i][j] == matrix[neighbor[0]][neighbor[1]]) {
            same++
        }
    }
    if(same >= 2) {
        let result = []
        for(let neighbor of neighborcells) {
            if(matrix[neighbor[0]][neighbor[1]] != undefined) {
                result.push(neighbor)
            }
        }
        result.push([i,j])
        return result
    }
    return []
}

function shiftRow(row) {
    for(let i = row.length-1; i >= 0; i--) {
        if(row[i] == 0) {
            let j = i
            while(row[j] == 0 && j > 0) {
                j--
            }
            if(row[j] == 0) {
                return
            } else {
                row[i] = row[j]
                row[j] = 0
            }
        }
    }
}

function solution(bubbles) {
    let transposed = transpose(bubbles)
    let explodingcells = []
    for(let i = 0; i < transposed.length; i++) {
        for(let j = 0; j < transposed[0].length; j++) {
            let neighbors = checkNeighbors(transposed, [i,j])
            if(neighbors.length > 0) {
                explodingcells.push(...neighbors)
            }
        }
    }
    for(let cell of explodingcells) {
        transposed[cell[0]][cell[1]] = 0
    }
    for(let row of transposed) {
        shiftRow(row)
    }
    return transpose(transposed)
}

let bubblemat = [
    [3,1,2,1],
    [1,1,1,4],
    [3,1,2,2],
    [3,3,3,4],
]

let exploded = solution(bubblemat)
exploded.forEach(row => console.log(row))
