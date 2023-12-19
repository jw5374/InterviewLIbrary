package main

import "strconv"

func LastVisitedIntegers(words []string) []int {
	visited := []int{}
	res := []int{}
	lastVisited := -1
	for _, word := range words {
		if word != "prev" {
			num, _ := strconv.Atoi(word)
			visited = append(visited, num)
			lastVisited = len(visited) - 1
			continue
		}
		if lastVisited != -1 {
			res = append(res, visited[lastVisited])
			lastVisited--
			continue
		}
		res = append(res, lastVisited)
	}
	return res
}
