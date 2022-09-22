// Given a string separate the vowels and consonants. print them in order of first occurrence.
function separateString(s) {
  let occurrences = {}
  let vowels = "aeiou"
  let vowelString = ""
  let consonantString = ""
  let split = s.replace(" ", "").toLowerCase().split("")
  for(let char of split) {
    if(occurrences[char] != undefined) {
      occurrences[char]++
    } else {
      occurrences[char] = 1
    }
  }
  for(let char of split) {
    if(occurrences[char] == undefined) {
      continue;
    }
    if(vowels.includes(char)) {
      vowelString += char.repeat(occurrences[char])
    } else {
      consonantString += char.repeat(occurrences[char])
    }
    delete occurrences[char]
  }
  return [vowelString, consonantString]
}

console.log(separateString("Sample Case"))
