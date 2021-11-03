user = {'name':'Arif','age':'22','launguage':'python'}
# print(user)
# dictionaries are unordered : so accessed using keys.
# print(user['name'])  # <---- to access name.
# can store any type of data 

users = {
    'user1' : {'name':'something','age':'something'},
    'user2' : {'name':'pwnable','age':'pwnable'},
    'user3' : {'name': 'victim', 'age':'victims age'}
}
# add data to dictionary 
user['name'] = 'change'
print(user)

#-----------------------------------------------------------------------------------#

# if 'name' in user:
#     print('present')
# else :
#     print('not there')


# # ------------------------------dict.values()
# if 'change' in user.values():
#     print('yess')
# else :
#     print('noo')
# # ?check data type if still wrong query ,

# --------------------------------------------------------------------------------#
# for i in user :
#     print(i)


# for i in user.values() :
#     print(i)

#dict values is sepetate type dict values : cannot change them 

# for i in user:
#     print(user[i])   <-----    can access values :


