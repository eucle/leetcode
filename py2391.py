def garbageCollection(garbage: list[str], travel: list[int]) -> int:
    minutes = 0
    for letter in 'GMP':
        for i in range(len(garbage) - 1, -1, -1):
            if letter in garbage[i]:
                minutes += sum(travel[:i])
                break
    return minutes + len(''.join(garbage))


print(garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
print(garbageCollection(["MMM", "PGM", "GP"], [3, 10]))
