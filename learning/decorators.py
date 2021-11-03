def square(a):
    return a*a


# s = square

# print(s(3))
# print(s)
# print(square)

l = [1,2,3,4,5]

# print(list(map(square,l)))

# def my_map(func, l):
#     new = []
#     for item in l:
#         new.append(func(item))
#     return new


# print(my_map(lambda a:a*a*a, l))


#----------------------------------------------------------------------#
#outer func and inner func ::


# def outer_func():
#     def inner():
#         print("this is inner func")
#     return inner

# hack = outer_func()
# hack()

#----------------------------------------------------------------------#

import time 
import functools

def decorator_func(any_func):
    @wraps(any_func)
    def wrapper(*argc, **kwarg):
        t1 = time.time()
        return any_func(*argc,**kwarg)
    return wrapper



