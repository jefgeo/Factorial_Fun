def factorial(value):
    value = int(value)              # non-integer values not allowed.
    if value >= 1:
        temp = 1
        for i in range(1, value+1):
            temp = temp * i
        return temp
    else:
        return None

def factorial_recursive(value):
    value = int(value)              # non-integer values not allowed.
    if value > 1:                   # recursively go from value to 1
        return value * factorial_recursive(value - 1)
    elif value == 1:                # Last value must be 1 if valid
        return value
    else:                           # return None for invalid
        return None


