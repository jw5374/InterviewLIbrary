const fs = require('fs')
const path = require('path')

const { findMaxPath } = require('./E18.js')

let trianglefile = fs.readFileSync(path.resolve(__dirname, 'p067_triangle.txt'), 'utf8')

let triangleData = []

trianglefile.split("\n").forEach(line =>  {
    let lineArray = line.split(" ").map(num => parseInt(num))
    triangleData.push(lineArray)
})

console.log(findMaxPath(triangleData, [0,0]))