def factor(number):
    factors = []
    number = int(number)
    if number in [-1, 0, 1]:
        factors.append(number)
    current_factor = 2
    while abs(number) > 1:
        while number % current_factor == 0:
            neg_flag = 1 if number > 1 else -1
            factors.append(current_factor * neg_flag)
            number = number / current_factor * neg_flag
        current_factor += (1 if current_factor % 2 == 0 else 2)
    return factors

def check_list(n, d):
    for number in n:
        if number % d != 0:
            return False
    return True

def greatest_common_factor(numbers):
    loop_value = abs(int(numbers[0]))
    # find the lowest value from list to start scan
    for number in numbers:
        number = abs(int(number))
        loop_value = number if number < loop_value else loop_value
    while loop_value >= 1 and not check_list(numbers, loop_value):
        loop_value -= 1
    return loop_value


def gather_factors(factors):
    gathered_factors = []
    i = factors[0]
    factor_count = 0
    for f in factors:
        if i == f:
            factor_count += 1
        else:
            gathered_factors.append([i, factor_count])
            factor_count = 1
            i = f
    gathered_factors.append([i, factor_count])

    return gathered_factors


def least_common_denominator(denominators):
    lcd = 1
    combined = {}
    for denominator in denominators:
        factors = gather_factors(factor(denominator))
        for f in factors:
            if f[0] in combined:
                if combined[f[0]] < f[1]:
                    combined[f[0]] = f[1]
            else:
                combined[f[0]] = f[1]
    for key in combined:
        lcd = lcd * key ** combined[key]
    return lcd


print(greatest_common_factor([12, 15]))

print(least_common_denominator([12, 15, 2, 9, 3, 7]))



