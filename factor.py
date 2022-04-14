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

