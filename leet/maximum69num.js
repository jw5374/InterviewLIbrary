/*
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
*/

function maximum69Number(num) {
  let numstring = num.toString().split("")
  for(let i = 0; i < numstring.length; i++) {
    if(numstring[i] == '6') {
      numstring[i] = '9'
      break
    }
  }
  return parseInt(numstring.join(""))
}

console.log(maximum69Number(9999))
