from typing import Any


def countBits(n: int) -> Any[int]:
    return (idx.bit_count() for idx in range(n + 1))


print(countBits(2))
print(countBits(5))
