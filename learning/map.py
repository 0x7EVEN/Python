numbers = [1,2,3,4,5,6]

def square(a):
    return a**2

# sq = list(map(square,numbers))
# <map object at 0x0000025023B1DFA0>

# print(sq)


# sq =list(map(lambda a : a*a , numbers))
# print(sq)

new_list = []
for num in numbers:
    new_list.append(square(num))
print(new_list)