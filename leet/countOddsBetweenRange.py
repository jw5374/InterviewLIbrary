def countOdds(low: int, high: int) -> int:
    odds = (high - low) // 2
    lowOdd = low % 2 != 0
    highOdd = high % 2 != 0
    odds += lowOdd + highOdd
    return odds if not (lowOdd and highOdd) else odds - 1

