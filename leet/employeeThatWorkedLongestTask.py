def hardestWorker(n: int, logs: list[list[int]]) -> int:
    longestEmp = -1
    longestTask = 0
    for i, log in enumerate(logs):
        if i == 0:
            longestEmp = log[0]
            longestTask = log[1]
            continue
        taskTime = log[1] - logs[i-1][1]
        if taskTime > longestTask:
            longestTask = log[1] - logs[i-1][1]
            longestEmp = log[0]
        elif taskTime == longestTask:
            longestEmp = log[0] if log[0] < longestEmp else longestEmp
    return longestEmp
