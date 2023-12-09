package main

func BuyChoco(prices []int, money int) int {
    mins := [2][2]int{{len(prices), 101}, {len(prices), 101}}
    for i, price := range prices {
        if price < mins[0][1] {
            mins[0][1] = price
            mins[0][0] = i
        }
    }
    for i, price := range prices {
        if i != mins[0][0] && price < mins[1][1] {
            mins[1][1] = price
            mins[1][0] = i
        }
    }
    diff := money - (mins[0][1] + mins[1][1])
    if diff < 0 {
        return money
    }
    return diff
}
