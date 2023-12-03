package main

func LargestGoodInteger(num string) string {
	res := ""
	maxVal := -1
	for i := 0; i < len(num) - 2; i++ {
		currNum := num[i:i+3]
		currVal := int(currNum[0] - 48)
		if currVal > maxVal && (currNum[0] == currNum[1] && currNum[1] == currNum[2]) {
			maxVal = currVal
			res = string(currNum)
		}
	}
	return res
}
