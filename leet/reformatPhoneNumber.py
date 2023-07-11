import re


def reformatNumber(number: str) -> str:
    stripped = re.sub("[- ]", "", number)
    end = 3 if len(stripped) % 3 == 0 else len(stripped) % 3
    res = []
    for i in range(0, len(stripped) - end, 3):
        res.append(stripped[i:i+3])
    res.append(stripped[-end:])
    if end == 1:
        res[-1] = res[-2][-1] + res[-1]
        res[-2] = res[-2][0:2]
    return "-".join(res)
