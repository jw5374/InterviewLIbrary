def dayOfYear(date: str) -> int:
    date = [int(d) for d in date.split("-")]
    # they really switched up the pattern between july and august -_-
    months = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
    leap = (date[0] % 4 == 0) if date[0] % 100 != 0 else (date[0] % 400 == 0)  # leap year if divisible by 4, but if divisible by 100, then must be also divisible by 400
    total = 0
    for m in range(1, date[1]):
        total += months[m]
    total += date[2] + leap if date[1] != 2 else date[2]
    return total


print(dayOfYear("2004-05-30"))

