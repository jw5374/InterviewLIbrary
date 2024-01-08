import math

f = open("p042_words.txt", "r")
words = f.readline().split(",")
words = [word.replace("\"", "") for word in words]

def calcTriangleNum(index: int) -> int:
	return (index * (index + 1)) / 2

def calcWordVal(word: str) -> int:
	val = 0
	for i in range(len(word)):
		val += ord(word[i]) - 64
	return val

def isTriangleNum(num: int) -> bool:
	potentialIndex = math.floor(math.sqrt(2 * num))
	return num == calcTriangleNum(potentialIndex)

def findTriangleWords(words: list[str]) -> int:
	res = 0
	for word in words:
		if isTriangleNum(calcWordVal(word)):
			res += 1
	return res

print(findTriangleWords(words))
