a = int(input("Enter the input 1?\n"))
b = int(input("Enter the input 2?\n"))


def find_gcd(aa, bb):
    num1 = aa
    num2 = bb
    res = min(num1, num2)
    while res > 0:
        if num1 % res == 0 and num2 % res == 0:
            break
        res = res - 1
    return res


answer = find_gcd(a, b)
print("The gcd of", a, "and", b, "is", answer)
