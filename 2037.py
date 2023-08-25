def minMovesToSeat(seats: list[int], students: list[int]) -> int:
    seats.sort()
    students.sort()
    return sum([abs(i - j) for i, j in zip(seats, students)])


print(minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
print(minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]))
print(minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]))
