package main

func SortPeople(names []string, heights []int) []string {
	sortArrays(names, heights, 0, len(heights))
	return names
}

func sortArrays(names []string, heights []int, low, high int) {
	size := high - low
	if size <= 9 {
		insertionSort(names, heights, low, high)
		return
	} else if low >= 0 && high >= 0 && low < high {
		pivot := partitionArrays(names, heights, low, high)
        sortArrays(names, heights, low, pivot)
        sortArrays(names, heights, pivot+1, high)
	}
}

func partitionArrays(names []string, heights []int, low, high int) int {
	split := heights[(low + high) / 2]
	i := low
	j := high
    for {
        for heights[i] < split {
            i++
        }
        for heights[j] > split {
            j--
        }
        if i >= j {
            return j
        }
		heights[i], heights[j] = heights[j], heights[i]
		names[i], names[j] = names[j], names[i]
    }
}

func insertionSort(names []string, heights []int, low, high int) {
	for i := low; i < high; i++ {
		itemIndex := i+1
        for itemIndex > low && heights[itemIndex - 1] > heights[itemIndex] {
			heights[itemIndex], heights[itemIndex-1] = heights[itemIndex-1], heights[itemIndex]
			names[itemIndex], names[itemIndex-1] = names[itemIndex-1], names[itemIndex]
            itemIndex--
        }
    }
}
