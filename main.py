import factorial
import factor

number = 18

print(factorial.factorial(number))
# print(factorial.factorial_recursive(number))


for i in range(-10, 10, 1):
    print(i, factor.factor(i))

print(factor.factor(factorial.factorial(number)))
