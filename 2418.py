def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    return [v for k, v in sorted(dict(zip(heights, names)).items(), reverse=True)]


print(sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
print(sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
