def countStudents(students: list[int], sandwiches: list[int]) -> int:
    pendingStudents = []
    [i, j] = [0, 0]
    while i < len(sandwiches) and j < len(students):
        if students[j] != sandwiches[i]:
            pendingStudents.append(students[j])
            j += 1
        else:
            i += 1
            while len(pendingStudents) > 0 and pendingStudents[-1] == sandwiches[i]:
                pendingStudents.pop()
                i += 1
            j += 1
    return len(pendingStudents)


print(countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))

