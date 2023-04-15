def maxNumberOfBalloons(text: str) -> int:
    balloonLetters = {
        "b": 0,
        "a": 0,
        "l": 0,
        "o": 0,
        "n": 0
    }
    minBalloons = len(text)
    for c in text:
        if c in balloonLetters:
            balloonLetters[c] += 1
    for key, value in balloonLetters.items():
        if key == "l" or key == "o":
            minBalloons = min(minBalloons, value // 2)
        else:
            minBalloons = min(minBalloons, value)
    return minBalloons
