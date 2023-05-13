def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
    bulkyDim = 10000
    bulkyVol = 1000000000
    isBulky = (length >= bulkyDim) or (width >= bulkyDim) or (height >= bulkyDim) or (length*width*height >= bulkyVol)
    isHeavy = mass >= 100
    if isBulky and isHeavy:
        return "Both"
    elif not (isBulky or isHeavy):
        return "Neither"
    else:
        return "Bulky" if isBulky else "Heavy"
