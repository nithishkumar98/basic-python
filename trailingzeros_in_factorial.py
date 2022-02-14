num = int(input("Enter the number?"))


def fact(n):
    res = 1
    for i in range(n, 0, -1):
        res = res * i
    return res


fact_res = fact(num)


def trailing_zero(n):
    count = 0
    while n % 10 == 0:
        count = count + 1
        n = n // 10
    return count


trail_count = trailing_zero(fact_res)
print("The trail count of factorial", num, "is", trail_count)
