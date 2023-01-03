def checkRecord(s: str) -> bool:
    absences = 0
    lates = 0
    i = 0
    while i < len(s) and absences < 2 and lates < 3:
        if s[i] == "L":
            lates += 1
            i += 1
            continue
        if s[i] == "A":
            absences += 1
        lates = 0
        i += 1
    if absences < 2 and lates < 3:
        return True
    return False


print(checkRecord("PPALLP"))

