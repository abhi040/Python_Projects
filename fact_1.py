# def fact_iterative(n):
#     fact = 1
#     for i in range(n):
#         fact=fact*(i+1)
#     return fact
#
# number=int(input("Enter the number: "))
# print(fact_iterative(number))
#

def fact_recursive(n):
    if n == 1:
        return 1
    else:
        return n*fact_recursive(n-1)

number=int(input("Enter the number: "))
print(fact_recursive(number))
