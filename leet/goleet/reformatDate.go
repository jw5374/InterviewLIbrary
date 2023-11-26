package main

import (
	"strings"
	"fmt"
)

var months map[string]int= map[string]int{
	"Jan": 1,
	"Feb": 2,
	"Mar": 3,
	"Apr": 4,
	"May": 5,
	"Jun": 6,
	"Jul": 7,
	"Aug": 8,
	"Sep": 9,
	"Oct": 10,
	"Nov": 11,
	"Dec": 12,
}

func ReformatDate(date string) string {
	dateSplit := strings.Split(date, " ")
	res := fmt.Sprintf("%s-%01d-%s", dateSplit[2], monthNum(dateSplit[1]), string(dateSplit[0][:len(dateSplit[0]) - 2]))

	return res
}

func monthNum(m string) int {
	res, _ := months[m]
	return res
}
