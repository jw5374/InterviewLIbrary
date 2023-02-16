def fizzBuzz(n: int) -> list[str]:
    res = []
    for x in range(1, n+1):
        val = ""
        if x % 3 == 0:
            val += "Fizz"
        if x % 5 == 0:
            val += "Buzz"
        val = val if val != "" else str(x)
        res.append(val)
    return res


print(fizzBuzz(5))

