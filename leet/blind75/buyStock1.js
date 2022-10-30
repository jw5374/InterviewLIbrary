function maxProfit(prices) {
  let [buy, sell] = [0,1]
  let max = 0
  while(sell < prices.length) {
    let profit = prices[sell] - prices[buy]
    if(profit < 0) {
      buy = sell
    }
    if(profit > max) {
      max = profit
    }
    sell++
  }
  return max
}


console.log(maxProfit([7,1,5,3,6,4]))
