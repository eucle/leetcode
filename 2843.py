def countSymmetricIntegers(low: int, high: int) -> int:
    res = 0
    for num in range(low, high + 1):
        length = len(str(num))
        if not length % 2:
            num_list = list(map(int, list(str(num))))
            res += sum(num_list[:int(length / 2)]) == sum(num_list[int(length / 2):])
    return res


print(countSymmetricIntegers(1, 100))
print(countSymmetricIntegers(1200, 1230))
