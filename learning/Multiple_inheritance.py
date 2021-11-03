class A: 
    def class_A_method(self):
        return "I am class A method"

    def hello(self):
        return "hello from class A"
class B: 
    def class_B_method(self):
        return "I am class B method"

    def hello(self):
        return "hello from class B"
class C(A,B):
    pass 

instance_C = C()

# print(instance_C.class_A_method())
# print(instance_C.class_B_method())
# print(instance_C.hello())

print(help(C))