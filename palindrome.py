n = int(input("Enter the number"))


def palindrome_check(num):
    temp = num
    res = 0
    while temp != 0:
        it = temp % 10
        res = res * 10 + it
        temp = temp // 10
    if num == res:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


palindrome_check(n)
