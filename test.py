import random

minR = 0
maxR = 127
symbols = [chr(i) for i in range(minR, maxR)]  # все символы ASCII
maxBase = maxR - minR  # система счисления, в которую мы переводим все числа


# Перевод из 10-ной в систему счисления с основанием base (для этого алгоритма - это 127-ная система)
def decimal_to_base(n, base, digits):
    if base < 2 or base > len(digits):
        raise ValueError(f"Base must be between 2 and {len(digits)}")
    if n == 0:
        return digits[0]

    result = ""
    negative = False
    if n < 0:
        negative = True
        n = abs(n)
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base
    if negative:
        result = "-" + result

    return result


# Перевод из системы счисления с основанием maxBase в систему счисления с основанием base (10-ная система)
def base_to_decimal(number, base, digits):
    if base < 2 or base > len(digits):
        raise ValueError(f"Base must be between 2 and {len(digits)}")

    decimal_number = 0
    power = 0

    for digit in reversed(number):
        if digit not in digits:
            raise ValueError("Invalid digit in the number")

        digit_value = digits.index(digit)
        decimal_number += digit_value * (base ** power)
        power += 1

    return decimal_number


def serialize(array):
    res = []
    for i in array:
        res.append(str(decimal_to_base(i, maxBase, symbols)))
    return ",".join(res)


def deserialize(string):
    array = string.split(',')
    res = []
    for i in array:
        res.append(int(base_to_decimal(i, maxBase, symbols)))
    return res


# ТЕСТЫ
v1 = [random.randint(1, 300) for _ in range(50)]
v2 = [random.randint(1, 300) for _ in range(100)]
v3 = [random.randint(1, 300) for _ in range(500)]
v4 = [random.randint(1, 300) for _ in range(500)]
v5 = [random.randint(1, 300) for _ in range(1000)]
v6 = [random.randint(1, 10) for _ in range(1000)]
v7 = [random.randint(10, 100) for _ in range(1000)]
v8 = [random.randint(100, 1000) for _ in range(1000)]

test = [v1, v2, v3, v4, v5, v6, v7, v8]

sumK = 0
for input_range in test:
    ser = serialize(input_range)
    des = deserialize(ser)

    input_range_str = ",".join(map(str, input_range))
    des_str = ",".join(map(str, des))
    sumK += len(ser) / len(input_range_str)

    print("Исходная строка: ", input_range_str)
    print("Сжатая строка: ", ser)
    print("Коэффициент сжатия: " + str(len(ser) / len(input_range_str)))

print("Средний коэффициент сжатия: " + str(sumK / len(test)))
