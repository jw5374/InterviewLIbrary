function twoSumIndices(nums, target) {
     for (let num = 0; num < nums.length; num++) {
        let remain = target - nums[num];
        let newnums = [...nums];
        newnums.splice(num, 1)
        if(newnums.indexOf(remain) != -1 && nums.indexOf(remain) != num) {
            return [num, nums.indexOf(remain)]
        } else if(newnums.indexOf(remain) != -1) {
            return [num, newnums.indexOf(remain)+1]
        }
    } 
}

function twoSumHash(nums, target) {
    let dict = {}
    for(let i = 0; i < nums.length; i++) {
       if(dict[nums[i]] != undefined) {
           dict[nums[i]].push(i)
       } else {
           dict[nums[i]] = [i]
       }
    }
    for(let i = 0; i < nums.length; i++) {
        let remaining = target - nums[i]
        if(dict[remaining] != undefined && (dict[remaining].length > 1 || remaining != nums[i])) {
            return [i, dict[remaining].pop()]
        }
    }
}

