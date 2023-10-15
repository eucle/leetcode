from collections import Counter


def bestHand(ranks: list[int], suits: list[str]) -> str:
    if len(set(suits)) == 1:
        return 'Flush'
    maximum = max(Counter(ranks).values())
    if maximum >= 3:
        return 'Three of a Kind'
    elif maximum == 2:
        return 'Pair'
    return 'High Card'
