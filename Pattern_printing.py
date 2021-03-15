def pypat(n):
    if my_bool:
        for i in range(0,n):
            for j in range(0, i+1):
                print("*", end="")
            print()
    else:
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print("*", end="")
            print()


n=int(input("Enter the input integer: "))
b=int(input("Enter 0 for false and 1 for true: "))
my_bool=bool(b)
pypat(n)

