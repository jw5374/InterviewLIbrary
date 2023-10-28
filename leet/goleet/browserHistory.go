package main

type BrowserHistory struct {
    History []string
    CurrentPage int
}


func BrowserHistoryConstructor(homepage string) BrowserHistory {
    home := append([]string{}, homepage)
    return BrowserHistory{ History: home, CurrentPage: 0 }
}


func (this *BrowserHistory) Visit(url string)  {
    this.History = this.History[:this.CurrentPage+1]
    this.History = append(this.History, url)
    this.CurrentPage++
}


func (this *BrowserHistory) Back(steps int) string {
    if this.CurrentPage - steps < 0 {
        this.CurrentPage = 0
    } else {
        this.CurrentPage -= steps
    }
    return this.History[this.CurrentPage]
}


func (this *BrowserHistory) Forward(steps int) string {
    if this.CurrentPage + steps > len(this.History) - 1 {
        this.CurrentPage = len(this.History) - 1
    } else {
        this.CurrentPage += steps
    }
    return this.History[this.CurrentPage]
}
