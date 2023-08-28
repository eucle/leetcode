def minOperations(boxes: str) -> list[int]:
    ans = []
    for i in range(len(boxes)):
        summ = 0
        for j in range(len(boxes)):
            if boxes[j] == '1':
                summ += abs(j - i)
        ans.append(summ)
    return ans


print(minOperations("110"))
print(minOperations("001011"))
