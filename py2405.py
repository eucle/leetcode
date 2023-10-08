def partitionString(s: str) -> int:
    counter: int = 1
    my_set: set[str] = set()
    for letter in s:
        if letter in my_set:
            counter += 1
            my_set = set()
        my_set.add(letter)
    return counter


print(partitionString('abacaba'))
