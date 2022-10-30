/*
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode
FOUND ON LINTCODE (LEETCODE PREMIUM QUESTION)

cannot submit to site without account unsure if complete solution
*/

function encode(strs) {
  let encoded = "" 
  for(let str of strs) {
    encoded += str.length + "=" + str
  }
  return encoded
}

function decode(str) {
  let splitted = str.split("")
  let decoded = []
  for(let i = 0; i < splitted.length; i++) {
    let j = i + 2
    let length = parseInt(splitted[i])
    let word = splitted.slice(j, j + length).join("")
    if(splitted[i+1] == "=") {
      decoded.push(word)
      i += 1 + length
    }
  }
  return decoded
}


let strings = ["lint","code","love","you"]
let encoded = encode(strings)
let decoded = decode(encoded)

console.log(encoded, decoded)

