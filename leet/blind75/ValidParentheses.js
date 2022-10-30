function isValid(s) {
  if(s.length % 2 != 0) {
    return false
  }
  brackets = {
    "(": ")",
    "[": "]",
    "{": "}"
  }
  let parenthesesStack = []
  for(let char of s.split("")) {
   if(brackets[char] != undefined) {
     parenthesesStack.unshift(char)
   } else {
     let peek = parenthesesStack[0]
     if(char == brackets[peek]) {
       parenthesesStack.shift()
     } else {
       return false
     }
   }
  }
  if(parenthesesStack.length == 0) {
    return true
  } else {
    return false
  }
}

console.log(isValid("(]"))
