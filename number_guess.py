num=15
i=5
while(i>0):
    # print("choices left", i)
    var=int(input("Enter the number of your choice: "))
    if var==num:
        print("Congratulations!You got the right guess")
        break
    elif var<num:
        print("Enter the greater number")
    elif var>num:
        print("Enter the smaller number")
    else:
        print("You have no choice left")
    i = i - 1
    print("choices left", i)


