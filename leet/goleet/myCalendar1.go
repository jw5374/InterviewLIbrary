package main

type MyCalendar struct {
    Events [][]int
}

func CalendarConstructor() MyCalendar {
    var e [][]int
    return MyCalendar{ Events: e }
}

func (this *MyCalendar) Book(start int, end int) bool {
    insertEvent := []int{start, end-1}
    if len(this.Events) == 0 {
        this.Events = append(this.Events, insertEvent)
        return true
    }
    var (
        insertI int = 0
        overlap bool = false
        insertIn bool = false
    )
    for i, e := range this.Events {
        insertI = i
        if (e[0] >= insertEvent[0] && e[1] <= insertEvent[1]) || (e[0] <= insertEvent[0] && e[1] >= insertEvent[0]) || (e[1] >= insertEvent[1] && e[0] <= insertEvent[1]) {
            overlap = true
            break
        }
        if e[0] > insertEvent[1] {
            insertIn = true
            break
        }
    }
    if overlap {
        return false
    }
    if !insertIn {
        insertI++
    }
    this.Events = insertAtIndex(this.Events, insertI, insertEvent)
    return true
}

func insertAtIndex(target [][]int, ind int, item []int) [][]int {
    if ind == len(target) {
        return append(target, item)
    }
    res := append(target[:ind+1], target[ind:]...)
    res[ind] = item
    return res
}
