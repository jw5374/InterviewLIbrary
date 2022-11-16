function convertToTitle(columnNumber) {
  let res = ""
  while(columnNumber > 0) {
    let digit = columnNumber % 26
    if(digit == 0) {
      res = String.fromCharCode(90) + res
      columnNumber = Math.floor(columnNumber / 26) - 1
    } else {
      res = String.fromCharCode(65 + (digit-1)) + res
      columnNumber = Math.floor(columnNumber / 26)
    }
  }
  return res
}

console.log(convertToTitle(729))
