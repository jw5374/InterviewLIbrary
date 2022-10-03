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
