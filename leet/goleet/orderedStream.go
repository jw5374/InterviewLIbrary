package main

type OrderedStream struct {
    TotalLength int
    Stream []string
    CurrentPtr int
}

func OrderedStreamConstructor(n int) OrderedStream {
    var ordStr OrderedStream = OrderedStream{
        TotalLength: n,
        Stream: make([] string, n),
        CurrentPtr: 0,
    }
    return ordStr
}


func (this *OrderedStream) Insert(idKey int, value string) []string {
    this.Stream[idKey-1] = value
    var startingPtr int = this.CurrentPtr
    for this.CurrentPtr < this.TotalLength && len(this.Stream[this.CurrentPtr]) != 0 {
        this.CurrentPtr++
    }
    return this.Stream[startingPtr:this.CurrentPtr]
}

