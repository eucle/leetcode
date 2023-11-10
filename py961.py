def repeatedNTimes(nums: list[int]) -> int:
    elems = set()
    for num in nums:
        if num in elems:
            break
        elems.add(num)
    return num
