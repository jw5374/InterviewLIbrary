package main

// too slow quadratic solution
// func distance(nums []int) []int64 {
//     indices := make(map[int][]int)
//     for i, num := range nums {
//         if _, exists := indices[num]; exists {
//             indices[num] = append(indices[num], i)
//         } else {
//             indices[num] = []int{ i }
//         }
//     }
//     res := make([]int64, len(nums))
//     if len(nums) == len(indices) {
//         return res
//     }
//     for i, num := range nums {
//         if len(indices[num]) == 1 {
//             continue
//         }
//         for _, index := range indices[num] {
//             res[i] += int64(math.Abs(float64(i) - float64(index)))
//         }
//     }
//     return res
// }

/* RAMBLING NOTES
[3, 1, 1, 2, 1, 1]
"3": [0]
"2": [3]
Focusing on "1" -
"1": [1, 2, 4, 5]
total offset from start of original array (1 + 2 + 4 + 5) = 12, this is the sum of all distances from origin (0)

We want to find sum of all distances from first occurrence = {index of first occurrence} * {length of indices} = 1 * 4 = 4
The distances for first element = ( 1-1, 2-1, 4-1, 5-1 )
We want to subtract this from total of all indices = 12 - 4 = 8 -> this is the distance of the first occurrence from all other occurrences ( 2-1 + 4-1 + 5-1 ) = 8
How to find the distances of second occurrence?
The new offset indices originating from first index = [0, 1, 3, 4], sum = 8
Distances from second occurrence = ( 0+1, 1-1, 3-1, 4-1 ) so we need to subtract 1 * 3 = 3 and add (1 * 1) = 1 from the total offset sum
8 - 3 = 5 + 1 = 6
Our offset indices = [1, 0, 2, 3], sum = 6
How to find the distances of third occurrence?
distances would be ( 2+1, 0+1, 1-1, 2-1 )


let's say we keep track of sum, first offsetted element, calculated offset, current occurrence and total occurrences
12 -> 1 -> 0 -> 0 -> 4 = 12 - ((1-0) * (4 - 0)) + ((1-0) * 0) = 8, new first == 0 (1-1, subtract because our current occurrence == 0), next offset = current index = 1
8 -> 0 -> 1 -> 1 -> 4 = 9 - ((2-1) * (4 - 1)) + ((2-1) * 1) = 8 - 3 + 1 = 6, new first == 1 (add the current calculated index to first element, 0 + 2), next offset = 2
5 -> 1 -> 2 -> 2 -> 4 = 5 - ((4-2) * (4 - 2)) + ((4-2) * 2) = 6 - 4 + 4 = 6, new first == 2 + 1, next offset = 4
5 -> 3 -> 4 -> 3 -> 4 = 5 - ((5-4) * (4 - 3)) + ((5-4) * 3) = 5 - 1 + 3 = 7

we don't need the first offsetted element actually


OVERALL FORMULA THAT SEEMS TO WORK:
DistanceSum(i) {
	indices := [...{all indices of nums[i]}]
	previousSumOfIndices := sum(indices)
	previousIndex := 0 (this is the 'offset')
	currentCalculatedIndex := i - previousIndex
	distanceFromCurrentPositionToEnd := len(indices)
	currentPositionOfOccurrence := some j where nums[indices[j]] == nums[i]

	newSumOfIndices := previousSumOfIndices - (currentCalculatedIndex * distanceFromCurrentPositionToEnd) + (currentCalculatedIndex * currentPositionOfOccurrence)
	newCurrentPositionOfOccurrence := currentPositionOfOccurrence + 1
	newIndex := i
	return newSumOfIndices (this is the distance off all other occurrences to i)
}
*/

func DistanceSums(nums []int) []int64 {
    indices := make(map[int][]int64)
    for i, num := range nums {
        castI := int64(i)
        if _, exists := indices[num]; exists {
            indices[num][0] += castI
            indices[num][3]++
        } else {
            indices[num] = []int64{
                castI, // will carry the sum of indices
                0, // will carry the 'offset' index
                0, // will carry the current position of occurrence
                1, // will carry the total number of occurrences of num
            }
        }
    }
    res := make([]int64, len(nums))
    if len(nums) == len(indices) {
        return res
    }
    for i, num := range nums {
        if len(indices[num]) == 1 {
            continue
        }
        castI := int64(i)
        index, _ := indices[num]
        currentCalculatedInd := (castI - index[1])
        res[i] = index[0] - (currentCalculatedInd * (index[3] - index[2])) + (currentCalculatedInd * index[2]) // set new sum of distances
        indices[num][0] = res[i] // set the new sum in hash table
        indices[num][1] = castI // set new offset index
        indices[num][2]++ // increment our current occurrence position
    }
    return res
}
