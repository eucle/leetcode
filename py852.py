def peakIndexInMountainArray(arr: list[int]) -> int:
    low, high = 0, len(arr) - 1
    while low < high:
        middle = (low + high) // 2
        if arr[middle - 1] < arr[middle] > arr[middle + 1]:
            return middle
        if arr[middle] < arr[middle - 1]:
            high = middle
        else:
            low = middle
    return middle
