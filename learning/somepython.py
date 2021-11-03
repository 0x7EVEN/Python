


print("wlcome to guess.it")
print ("you will win if you guess it correctly !")
win = 86
num_ent = int(input("Enter the number : "))
count = 1 
game_end = False
if num_ent:
    while not game_end :
        if num_ent == win :
            print("Yooooooooouuuuuuuu  Wwwwwwwoooooooonnnnnnnnnnn!!!!!")
            print (f"yyyeeeessss!!! you guessed it right in {count} attempts.")
            print("\n")
            print (r"FLAG{right_gessing_FLAG_you_got}") 
            
            print("\n")
            game_end = True
        else :
            if num_ent < win  : 
                print("you guessed it low add some.")
            else :
                print ("you guessed it high !! sub some.")
            count += 1
            num_ent = int(input("Enter  again : "))
    
    
else : 
    print("enter something !! are you finding bugs ?")