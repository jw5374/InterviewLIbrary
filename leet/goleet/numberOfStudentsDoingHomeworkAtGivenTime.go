package main

func BusyStudent(startTime []int, endTime []int, queryTime int) int {
	res := 0
	for i, time := range endTime {
		if time >= queryTime && startTime[i] <= queryTime {
			res++
		}
	}
	return res
}
