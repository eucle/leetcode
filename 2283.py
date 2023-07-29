def digitCount(num: str) -> bool:
    for key, value in enumerate(num):
        if num.count(str(key)) != int(value):
            return False
    return True


print(digitCount("1210"))
print(digitCount("030"))
