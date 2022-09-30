const { swap } = require('../viewLib/utils.js')

// assuming matrix is square
function transpose(mat) {
  for(let i = 0; i < mat.length; i++) {
    for(let j = i; j < mat.length; j++) {
      let temp = mat[i][j]
      mat[i][j] = mat[j][i]
      mat[j][i] = temp
    }
  }
}

function reverse(arr) {
  let i = 0
  let j = arr.length-1
  while(i < j) {
    swap(i, j, arr)
    i++
    j--
  }
}

function rotateImage(matrix) {
  reverse(matrix)
  transpose(matrix) 
  // return matrix
}

console.log(rotateImage([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
console.log(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))
