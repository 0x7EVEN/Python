    # def add(a,b):
        # return a+b
    #if user passes other type instead of int then we want to show error:

# def add(a,b):
#     if (a,b):
#         if (type(a)==int and type(b)==int):
#             return a+b
#         else :
#             return "enter the value in integer !"
#     else : 
#         return "you didnt entered anything !"
# print(add("awe",6))


#RAise_ERRor :::



# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError("You didn\'t entered right type!")

# print(add(2,'s'))

class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        raise NotImplementedError("You to define this in subclass!")

    
class  dog(Animal):
    def __init__(self,name,breed):
        return 