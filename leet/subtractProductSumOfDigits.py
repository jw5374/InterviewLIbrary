def subtractProductAndSum(n: int) -> int:
    sumOfDig = 0
    prodOfDig = 1
    while n > 0:
        currDig = n % 10
        sumOfDig += currDig
        prodOfDig *= currDig
        n //= 10
    return prodOfDig - sumOfDig


print(subtractProductAndSum(4421))

