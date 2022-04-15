import factorial
import factor

number = 18
print(factorial.factorial(number))
# print(factorial.factorial_recursive(number))
print(factor.get_factors(factorial.factorial(number)))

for i in range(-10, 10, 1):
    print(i, factor.get_factors(i))

print(factor.greatest_common_factor([5, 15]))

print(factor.least_common_denominator([12, 15, 2, 9, 3, 7]))
