def reorderSpaces(text: str) -> str:
    lst, res = text.split(), ''
    if len(lst) > 1:
        gap = text.count(' ') // (len(lst) - 1)
        for word in lst:
            res += word + ' ' * gap
        return res.rstrip(' ') + ' ' * (text.count(' ') % (len(lst) - 1))
    return text.strip(' ') + ' ' * text.count(' ')


print(reorderSpaces("  this   is  a sentence "))
print(reorderSpaces(" practice   makes   perfect"))
