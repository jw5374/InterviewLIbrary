function isAnagram(s, t) {
    if(s.length != t.length) {
        return false
    }
    s = s.split("").sort()
    t = t.split("").sort()
    for(let i = 0; i < s.length; i++) {
        if(s[i] != t[i]) {
            return false
        }
    }
    return true
}

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
var groupAnagrams = function(strs) {
    let groups = []
    for(let i = strs.length-1; i >= 0; i--) {
        let local = [strs.pop()]
        for(let j = i-1; j >= 0; j--) {
            if(isAnagram(local[0], strs[j])) {
                local.push(strs.splice(j, 1)[0])
                i--
            }
        }
        groups.push(local)
    }
    return groups
};
