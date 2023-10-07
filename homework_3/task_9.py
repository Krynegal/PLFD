def convert_to(number, base, upper=False): #конвертация только из десятичной системы, а по условию требуется из произвольной от 2 до 16
    digits = '0123456789abcdef'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


print(convert_to(199, 16))
