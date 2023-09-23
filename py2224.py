def convertTime(current: str, correct: str) -> int:
    cnt = 0
    time = (int(correct[:2]) * 60 + int(correct[3:]) -
            (int(current[:2]) * 60 + int(current[3:])))
    while time:
        if time > 59:
            time -= 60
        elif time > 14:
            time -= 15
        elif time > 4:
            time -= 5
        else:
            time -= 1
        cnt += 1
    return cnt
