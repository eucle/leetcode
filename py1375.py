def numTimesAllBlue(flips: list[int]) -> int:
    maximum = 0
    cnt = 0
    for i in range(len(flips)):
        if flips[i] > maximum:
            maximum = flips[i]
        if maximum == i + 1:
            cnt += 1
    return cnt
