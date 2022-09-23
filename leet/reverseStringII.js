// 541. Reverse String II
/*
  Given a string s and an integer k,
  reverse the first k characters for every 2k characters counting from the start of the string.
  
  If there are fewer than k characters left, reverse all of them. 
  If there are less than 2k but greater than or equal to k characters,
  then reverse the first k characters and leave the other as original.
*/
// definitely not a willfully obtuse problem statement, extremely helpful with software engineering candidate pruning.

function reverse(start, end, arr) {
    let i = start;
    let j = end;
    while(i < j) {
        let temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i++
        j--
    }
}

function reverseStringTwo(s, k) {
    let split = s.split("")
    for(let i = 0; i < split.length; i+=(2*k)) {
        reverse(i, (i+k)-1, split)
    }
    return split.join("")
};

console.log(reverseStringTwo("abcdefg", 2))
