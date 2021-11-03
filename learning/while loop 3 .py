print("Welcome to count !")

someinput = input("Enter the string to CHAR - count : ")

if someinput:
    i = 0
    temp = ""
    while i < len(someinput):
        
        if someinput[i] not in temp :
            temp += someinput[i]
            result = someinput.count(someinput[i])
            print(f"the result  {someinput[i]} :: {result}")
        i += 1
else : 
    print("You not entered anything :p ")