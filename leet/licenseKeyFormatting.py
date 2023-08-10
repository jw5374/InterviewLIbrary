def licenseKeyFormatting(s: str, k: int) -> str:
    filtered = s.replace("-", "").upper()
    leftover = len(filtered) % k
    newString = []
    if leftover != 0:
        newString.append(filtered[0:leftover])
    for i in range(leftover, len(filtered), k):
        newString.append(filtered[i:i+k])
    return "-".join(newString)
