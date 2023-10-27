package main

type RLEIterator struct {
    CurrentElement int
    RLEArray []int
}

func RLEConstructor(encoding []int) RLEIterator {
    return RLEIterator{ CurrentElement: 0, RLEArray: encoding }
}

func (this *RLEIterator) Next(n int) int {
    for n > 0 {
        if this.CurrentElement >= len(this.RLEArray) {
            return -1
        }
        if this.RLEArray[this.CurrentElement] == 0 {
            this.CurrentElement += 2
            continue
        }
        if this.RLEArray[this.CurrentElement] >= n {
            this.RLEArray[this.CurrentElement] -= n
            return this.RLEArray[this.CurrentElement + 1]
        }
        if this.RLEArray[this.CurrentElement] < n {
            temp := this.RLEArray[this.CurrentElement]
            this.RLEArray[this.CurrentElement], n = 0, n - temp
            this.CurrentElement += 2
        }
    }
    return this.RLEArray[this.CurrentElement + 1]
}
