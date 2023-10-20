def wateringPlants(plants: list[int], capacity: int) -> int:
    steps, balance = 0, capacity
    for key, value in enumerate(plants):
        if balance < value:
            balance = capacity - value
            steps += key * 2 + 1
        else:
            balance -= value
            steps += 1
    return steps


print(wateringPlants([2, 2, 3, 3], 5))
print(wateringPlants([1, 1, 1, 4, 2, 3], 4))
print(wateringPlants([7, 7, 7, 7, 7, 7, 7], 8))
