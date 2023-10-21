package main

import "strconv"

func ConvertToBase7(num int) string {
    return strconv.FormatInt(int64(num), 7)
}
