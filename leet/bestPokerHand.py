hands = {
        1: "High Card",
        2: "Pair",
        3: "Three of a Kind"
    }


def bestHand(ranks: list[int], suits: list[str]) -> str:
    rankOccs = {}
    for rank in ranks:
        if rank in rankOccs:
            rankOccs[rank] += 1
        else:
            rankOccs[rank] = 1
    maxRanks = max(rankOccs.values())
    return hands[maxRanks if maxRanks <= 3 else 3] if len(set(suits)) != 1 else "Flush"

