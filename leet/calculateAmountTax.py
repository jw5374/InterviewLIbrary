def calculateTax(brackets: list[list[int]], income: int) -> float:
    currBrack = 0
    totalTax = 0.0
    i = 0
    while income > 0 and i < len(brackets):
        bracket = brackets[i]
        currIncome = bracket[0] - currBrack
        percentage = bracket[1] / 100
        dollars = currIncome if income - currIncome >= 0 else income
        totalTax += dollars * percentage
        income -= currIncome
        currBrack = bracket[0]
        i += 1
    return totalTax


print(calculateTax([[3,50],[7,10],[12,25]], 10))

