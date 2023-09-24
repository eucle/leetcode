def findOcurrences(text: str, first: str, second: str) -> list[str]:
    lst = text.split()
    return [lst[i + 2] for i in range(len(lst) - 2)
            if lst[i] == first and lst[i + 1] == second]
