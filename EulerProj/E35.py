sieve = [x for x in range(2, 1000001)]

i = 0
while i < len(sieve):
    if sieve[i] is None:
        i += 1
        continue
    j = i + sieve[i]
    while j < len(sieve):
        if sieve[j] is None:
            j += sieve[i]
            continue
        sieve[j] = None
        j += sieve[i]
    i += 1

sieve = set(sieve)

circularPrimes = 0

for num in sieve:
    if num is None:
        continue
    rotations = str(num) * 2
    numLen = len(rotations) // 2
    print(rotations, numLen)
    for i in range(numLen):
        if int(rotations[i:i+numLen]) not in sieve:
            break
    else:
        circularPrimes += 1

print(circularPrimes)
