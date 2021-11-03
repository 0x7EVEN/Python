names = ['name' , 'somename' ,'some name' ,'suranme' ] 
pos = 0 

# for name in names:
#     print(f"{pos} : {name}")
#     pos+= 1 


# for pos, name  in enumerate(names):
#     print(f"{pos} : {name}")

def func(l, target):
    if l:
        for pos, name in enumerate(l):
            if name == target :
                return pos
        return -1
    else :
        print ("enter something")

l = ['abc','name', 'enumerate', 'sdfsads']
print(func(l ,'enumerate'))    
