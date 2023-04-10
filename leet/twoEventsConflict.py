def haveConflict(event1: list[str], event2: list[str]) -> bool:
    e1Split = [int("".join(x.split(":"))) for x in event1]
    e2Split = [int("".join(x.split(":"))) for x in event2]
    return not ((e1Split[1] < e2Split[0]) != (e2Split[1] < e1Split[0]))
