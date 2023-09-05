def findOcurrences(text: str, first: str, second: str) -> list[str]:
    words = text.split(" ")
    res = []
    for i in range(len(words) - 2):
        if f"{words[i]} {words[i+1]}" == f"{first} {second}":
            res.append(words[i+2])
    return res
