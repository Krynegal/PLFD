def convert_to(number, base, upper=False):
    digits = '0123456789abcdef'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


print(convert_to(199, 16))
