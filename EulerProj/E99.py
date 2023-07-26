import csv
from typing import List

baseExpPairs = []

with open('0099_base_exp.txt', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        baseExpPairs.append([int(x) for x in row])


# can compare powers by normalizing the exponents through division
def comparePowers(a: List[int], b: List[int]) -> List[int]:
    reducedA = [a[0], a[1]]
    reducedB = [b[0], b[1]]
    if a[1] > b[1]:
        reducedA[1] /= reducedB[1]
        reducedB[1] = 1
    else:
        reducedB[1] /= reducedA[1]
        reducedA[1] = 1
    reducedA = reducedA[0] ** reducedA[1]
    reducedB = reducedB[0] ** reducedB[1]
    print(reducedA, reducedB)
    return a if reducedA > reducedB else b


currGreatest = comparePowers(baseExpPairs[0], baseExpPairs[1])

for i in range(2, len(baseExpPairs)):
    currGreatest = comparePowers(currGreatest, baseExpPairs[i])

print(currGreatest)

