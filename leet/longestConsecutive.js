
/*
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
*/

function longestConsecutiveSequence(nums) {
    // put all numbers into hashtable
    let table = {}
    for(let num of nums) {
        table[num] = 1
    }
    // check contiguous values from hash
    let maxCont = 0
    for(let num of nums) {
        if(table[num-1] == undefined) {
            let local = 0
            let lNum = num
            while(table[lNum] != undefined) {
                local++
                lNum++
            }
            if(local > maxCont) {
                maxCont = local
            }
        }
    }
    return maxCont
}

console.log(longestConsecutiveSequence([0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]))
