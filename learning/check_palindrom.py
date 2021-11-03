# print ("welcome to palindrom")
# some = input("Enter : ")
# def somefunction(some):    
#     return some == some[::-1]
# print(somefunction(some))



something = input("enter 3 numbers :")
A,B,C = something.split(",")#.Map(int)
a = int(A)
b = int (B)
c = int (C)
if a > b : 
    if a > c :
        print(a)
    else :
        print(c)
else :
    if c > b :
        print(c)
    else :
        print(b)