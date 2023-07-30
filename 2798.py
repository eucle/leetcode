hours = [0, 1, 2, 3, 4]
target = 2
print(len(tuple(filter(lambda hour: hour >= target, hours))))
