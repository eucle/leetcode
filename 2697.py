def makeSmallestPalindrome(s: str) -> str:
    lst = list(s)
    for i in range(len(lst) // 2):
        r_letter = lst[~i]
        if lst[i] != r_letter:
            if lst[i] > r_letter:
                lst[i] = r_letter
            else:
                lst[~i] = lst[i]
    return "".join(lst)


print(makeSmallestPalindrome('egcfe'))
print(makeSmallestPalindrome('abcd'))
print(makeSmallestPalindrome('seven'))
