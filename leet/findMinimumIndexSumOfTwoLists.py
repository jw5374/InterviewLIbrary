def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    hashed = {}
    minSum = len(list1) + len(list2)
    minWords = []
    for i, word in enumerate(list1):
        hashed[word] = i
    for i, word in enumerate(list2):
        if word in hashed:
            minSum = min(minSum, hashed[word] + i)
    for i, word in enumerate(list2):
        if word in hashed and minSum == i + hashed[word]:
            minWords.append(word)
    return minWords
