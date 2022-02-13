num = int(input("Enter the number to be counted??"))


def count_digit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    print(count)


count_digit(num)
