def countBits(n: int) -> list[int]:
    return [i.bit_count() for i in range(n + 1)]


print(countBits(2))
print(countBits(5))
