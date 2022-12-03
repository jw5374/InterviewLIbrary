def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
	totalPoisoned = duration
	for i in range(len(timeSeries)-1):
		timeDiff = timeSeries[i+1] - timeSeries[i]
		if timeDiff < duration:
			totalPoisoned += timeDiff
			continue
		totalPoisoned += duration
	return totalPoisoned

print(findPoisonedDuration([1,3], 2))
