def sumOddLengthSubarrays(arr: list[int]) -> int:
    length = len(arr)
    return sum([sum(arr[i:j+1]) for i in range(length) for j in range(i, length, 2)])


print(sumOddLengthSubarrays([1, 4, 2, 5, 3]))
print(sumOddLengthSubarrays([1, 2]))
print(sumOddLengthSubarrays([10, 11, 12]))
