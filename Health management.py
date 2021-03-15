import datetime
def gettime():
    return datetime.datetime.now()
def take(var2):
    if var2==1:
        var4=int(input("Press:\n 1 --> Food\n 2 --> Exercise\n"))
        if var4==1:
            value=input("Enter Food: ")
            try:
                f = open("harry_food.txt","a")
                f.write(str([str(gettime())])+": "+value +"\n")
                print("successfully added")
            finally:
                f.close()
        elif var4 == 2:
            value=input("enter Exercise: ")
            try:
                f = open("harry_exercise.txt","a")
                f.write(str([str(gettime())])+": "+value +"\n")
                print("successfully added")
            finally:
                f.close()
    elif var2==2:
        var4=int(input("Press:\n 1--> Food\n 2-->Exercise\n"))
        if var4==1:
            value=input("enter Food: ")
            try:
                f=open("hammad_food.txt","a")
                f.write(str([str(gettime())])+": "+value +"\n")
                print("successfully added")
            finally:
                f.close()
        elif var4==2:
            value=input("enter Exercise: ")
            try:
                f=open("hammad_exercise.txt", "a")
                f.write(str([str(gettime())]) + ": " + value  + "\n")
                print("successfully added")
            finally:
                f.close()
    elif var2==3:
        var4=int(input("Press:\n 1--> Food\n 2-->Exercise\n"))
        if var4==1:
            value=input("enter Food: ")
            try:
                f=open("rohan_food.txt","a")
                f.write(str([str(gettime())])+": "+value +"\n")
                print("successfully added")
            finally:
                f.close()
        elif var4==2:
            value=input("enter Exercise")
            try:
                f=open("rohan_exercise.txt","a")
                f.write(str([str(gettime())])+": "+value +"\n")
                print("successfully added")
            finally:
                f.close()
def retrieve(var3):
    if var3==1:
        var4=int(input("Press:\n 1-->Food\n 2-->Exercise\n"))
        if var4==1:
            try:
                f=open("harry_food.txt", "r")
                for i in f:
                    print(i)
            finally:
                f.close()
        elif var4==2:
            try:
                f=open("harry_exercise.txt", "r")
                for i in f:
                    print(i)
            finally:
                f.close()
    elif var3==2:
        var4=int(input("Press:\n 1-->Food\n 2-->Exercise\n"))
        if var4==1:
            try:
                f=open("hammad_food.txt", "r")
                for i in f:
                    print(i)
            finally:
                f.close()
        elif var4==2:
            try:
                f=open("hammad_exercise.txt", "r")
                for i in f:
                    print(i)
            finally:
                f.close()
        elif var4==3:
            var4=int(input("Press:\n 1-->Food\n 2-->Exercise\n"))
            if var4==1:
                try:
                    f=open("rohan_food.txt", "r")
                    for i in f:
                        print(i)
                finally:
                    f.close()
            elif var4==2:
                try:
                    f=open("rohan_exercise.txt", "r")
                    for i in f:
                        print(i)
                finally:
                    f.close()
    else:
        print("Please enter valid input (Harry, Hammad, Rohan)")

print("health management system: ")
var1=int(input("What you want to do:\n 1)log:\n 2)retrieve:\n"))
if var1==1:
    var2=int(input("Press:\n 1 --> harry\n 2 --> hammad\n 3 --> rohan\n"))
    take(var2)
else:
    var3=int(input("Press:\n 1 --> harry\n 2 --> hammad\n 3 --> rohan\n"))
    retrieve(var3)

