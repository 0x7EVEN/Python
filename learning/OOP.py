# #e.g.  list class
# #list object 
# #method 



# #convention :: use capital letter (1st) in class.__name__
# #how to create ? : class Thisisclass:

# class Person:
#     def __init__(self, first_name,last_name,age):
#         #instance variables
#         print("at this instance this is called")
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age


# p1 = Person("Arif", "Shaikh", "24")
# p2 = Person("bro", "same", "almost")

# print(p1.first_name)
# print(p2.first_name)

#----------------------------------------------------------------------------------------#




# class Laptop:
#     def __init__(self,brand,name,Price):
#         self.brand = brand
#         self.name = name
#         self.Price = Price 

# val1 = Laptop("8", "1000", "30000")

# print(val1.brand)


#----------------------------------------------------------------------------------#


# python instance /object
#l = list is instance of class L ; where l.pop() is method of instance ::

# class Person:
#     def __init__(self, first_name,last_name,age):
#         #instance variables
#         print("at this instance this is called")
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"



# p1 = Person("name", "last name", 24)
# print(Person.full_name(p1))

# class Laptop:
#     def __init__(self,brand,name,Price):
#         self.brand = brand
#         self.name = name
#         self.Price = Price 
    
#     def discount(self,n):
#         return (self.Price -(n*self.Price/100))
# val1 = Laptop("8", "1000", 30000)
# print(val1.discount(5))


#------------------------------------------------------------------------------------#

class Person:
    def __init__(self, first_name,last_name,age):
        #instance variables
        print("at this point , instance this is called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


p1 = Person("Arif", "Shaikh", 22)
p2 = Person("Anam", "Shaikh", 24)
























