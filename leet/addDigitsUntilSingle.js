function addDigits(num) {
  if(num == 0) {
    return num
  }
  if(num % 9 == 0) {
    return 9 
  }
  return num % 9
}

/********* naive linear solution **********/
function addDigitsNaive(num) {
  let sum = basicDigitSum(num)
  while(sum > 9) {
    sum = basicDigitSum(sum)
  }
  return sum
}

function basicDigitSum(num) {
  let sum = 0
  while(num != 0) {
    sum += num % 10
    num = Math.floor(num / 10)
  }
  return sum
}
/*******************/

console.log(addDigits(38))
