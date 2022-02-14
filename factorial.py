num = int(input("Enter the number \n"))


def find_factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i
    return fact


def find_factorial_iter(n):
    if n == 0:
        return 1
    return n * find_factorial(n - 1)


res = find_factorial(num)
print("The factorial of", num, "is", res)

result = find_factorial_iter(num)
print("The factorial of", num, "is", result)
