package main

import "sort"

func FindLeastNumOfUniqueInts(arr []int, k int) int {
    occs := make(map[int]int)
    for i := 0; i < len(arr); i++ {
        if _, exists := occs[arr[i]]; exists {
            occs[arr[i]]++
        } else {
            occs[arr[i]] = 1
        }
    }
    var sortableNums [][]int
    for num, occ := range occs {
        sortableNums = append(sortableNums, []int{ num, occ })
    }
    sort.Slice(sortableNums, func(i, j int) bool {
        return sortableNums[i][1] < sortableNums[j][1]
    })
    for i, num := range sortableNums {
        if num[1] <= k {
            k -= num[1]
            continue
        } 
        return len(sortableNums) - i
    }
    return 0
}
