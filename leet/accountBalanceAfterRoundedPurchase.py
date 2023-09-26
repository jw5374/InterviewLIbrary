def accountBalanceAfterPurchase(purchaseAmount: int) -> int:
    digit = purchaseAmount % 10
    amount = purchaseAmount - digit
    return 100 - amount if digit < 5 else 100 - (amount + 10)
