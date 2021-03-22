# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# number=int(input("Enter the number: "))
# print(fibonacci(number))


def fib(n):
    """
    0=>a
    1=>b  =>a
    1=>c=>a+b  =>b
    2
    3
    5
    8
    13

    :param n:
    :return:
    """
    a = 0
    b = 1
    if n==0:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2, n):
        c = a+b
        a = b
        b = c
        print(c)

number=int(input("Enter range: "))
fib(number)

