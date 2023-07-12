def isStrictlyPalindromic(n: int) -> bool:
    def convert_to(number, base, upper=False):
        digits = '0123456789abcdefghijklmnopqrstuvwxyz'
        if base > len(digits):
            return None
        result = ''
        while number > 0:
            result = digits[number % base] + result
            number //= base
        return result.upper() if upper else result

    for i in range(2, n - 1):
        res = convert_to(n, i)
        if str(res) != str(res)[::-1]:
            return False
    return True


print(isStrictlyPalindromic(9))
print(isStrictlyPalindromic(4))
