num = input("Enter a number : ")

if num:

    i = 1
    total = 0
    while i <= int(num):
        total = total + i
        i += 1
    print(total)
else:
    print ("input Error !")