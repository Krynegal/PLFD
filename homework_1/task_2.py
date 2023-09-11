import math

num1, num2 = map(int, input("Введите два числа: ").split())

print(
    "{num1} + {num2} = {add}\n"
    "{num1} - {num2} = {sub}\n"
    "{num1} * {num2} = {mul}\n"
    "{num1} / {num2} = {div}\n"
    "{num1} // {num2} = {div_int}\n"
    "{num1} % {num2} = {mod}\n"
    "{num1} ** {num2} = {degree}\n"
    "log10({num1}) = {num1_log10}\n"
    "log10({num2}) = {num2_log10}\n".format(
        num1=num1,
        num2=num2,
        add=num1 + num2,
        sub=num1 - num2,
        mul=num1 * num2,
        div=round(num1 / num2, 2),
        div_int=num1 // num2,
        mod=num1 % num2,
        degree=num1 ** num2,
        num1_log10=round(math.log10(num1), 2),
        num2_log10=round(math.log10(num2), 2),
    )
)

print(
    "{num1} < {num2}: {lt}\n"
    "{num1} <= {num2}: {le}\n"
    "{num1} > {num2}: {gt}\n"
    "{num1} >= {num2}: {ge}\n"
    "{num1} != {num2}: {ne}\n"
    "{num1} == {num2}: {eq}".format(
        num1=num1,
        num2=num2,
        lt=num1 < num2,
        le=num2 <= num2,
        gt=num1 > num2,
        ge=num1 >= num2,
        ne=num1 != num2,
        eq=num1 == num2,
    )
)
