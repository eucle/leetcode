def minPartitions(n: str) -> int:
    return max(map(int, set(n)))


print(minPartitions("32"))
print(minPartitions("82734"))
print(minPartitions("27346209830709182346"))
