def selfDividingNumbers(left: int, right: int) -> list[int]:
    res = []
    for num in range(left, right + 1):
        flag = True
        cnt = 0
        digits = str(num)
        for digit in digits:
            if not int(digit):
                flag = False
                break
            if not num % int(digit):
                cnt += 1
        if not flag:
            continue
        elif len(str(num)) == cnt:
            res.append(num)
    return res
