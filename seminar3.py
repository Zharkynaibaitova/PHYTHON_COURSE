import random
# a = [1, 2, 3]
# b = a.copy()
# c = a
# a.append(4)
# b.append(5)
# c.append(6)
# print(a)
# print(b)
# print(c)
# print(id(a))
# print(id(b))
# print(id(c))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# from copy import deepcopy

# a = [1, 2, 3, [1, 2, 3]]
# b =deepcopy(a)

# a[3][1] = 9
# print(a)
# print(b)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# my_list = [1, 2, 3]
# my_string = '123'
# print(my_list[1])
# print(my_string[1])
# ++++++++++++++++++++++++++++++++++++++++++

# my_list = [1, 2, 3]
# my_string = '123'
# my_string = list(my_string)
# print(my_list)
# print(my_string)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# my_list = [1, 2, 3, 4]
# del_element = my_list.pop(2)
# print(my_list)
# print(del_element)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# my_list = [1, 2, 3, 4, 2,7, 8, 2]

# print(my_list.count(2))
# print(my_list)
      
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# my_list = [1, 2, 3, 4, 2,7, 8, 2]

# print(my_list.index(7))
# print(my_list)
# +++++++++++++++++++++++++++++++++++++++++

# my_list = [1, 2, 3, 4, 2,7, 8, 2]
# print(my_list[1:3:1])
# ++++++++++++++++++++++++++++++++++++++++++++++

# my_list = ['1', '2', '3', '4', '2','7', '2']
# print('hgygfyfy '.join(my_list))
# +++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   КОРТЕЖ   +++++++++++++++++++++++++++++++++++

# my_tuple = (1, 2, 3, 'r', [1,2,3,4])
# my_tuple[-1][-1] = 'AAAAAA'
# print(my_tuple)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++

# my_tuple = (1, 2, 3, 'r')
# dig1, dig2, dig3, let = my_tuple
# print(dig1)
# print(dig2)
# print(dig3)
# print(let)
# ++++++++++++++++++++++++++++++++
# my_tuple = (1, 2, 3, 'r')
# print(my_tuple, sep='\n', end='ppp')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ МНОЖЕСТВО++++++++++++++++++++++++++++++++++++++++

# my_set = {1,2,3,4,5,6,6}
# my_set.add(7)
# print(my_set)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++ СЛОВАРЬ++++++++++++++++++++++++++++++++++++++

# my_dict = {'Key' : {1234: {'key': 900}}}

# # print(my_dict.get('Key').get(1234).get('key'))
# print(my_dict.get('Key').get(1234))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# my_dict = {'ONE': 1, 2: 'Two', 3: 'ТРИ'}

# my_dict[4] = 'FOUR'  # добавление нового элемента
# print(my_dict)

# # print(my_dict['ONE'])
# # print(my_dict[2])
# # # print(my_dict[1])   # Ошибка
# # print(my_dict.get(1))

# print(my_dict.get(4, 'Нет такого элемента'))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# my_dict = {'ONE': 1, 2: 'Two', 3: 'ТРИ'}
# new_dict = {'ONE': 10, 2: 'Two!', 4: 'ЧКТЫРЕ'}


# # my_dict.update(new_dict)
# # print(my_dict)

# keys = {'One', 2, 3}
# print(my_dict.fromkeys(keys, 'Пусто'))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Итерация+++++++++++

# my_dict = {'ONE': 1, '2': 'Two', 3: 'ТРИ'}
# new_dict = {'ONE': 10, 2: 'Two!', 4: 'ЧКТЫРЕ'}

# # for i in my_dict.keys():
# #     print(i)
      
# # for i in my_dict.values():
# #     print(i)

# # for i in my_dict.items():
# #     print(i)

# for key, value in my_dict.items():
#     if key.isdigit():
#         print(value)
# ++++++++++++++++++++++++++++++++++++++++++++++++МАССИВЫ++++++++++++++++++++

# from array import *

# my_array = array('i', (1,2,3,4,5,6,77,8,9,10))
# print(my_array)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# my_list = []

# for i in range(10):
#     my_list.append(i)

# print(my_list)   # Это можно записать так:


# my_list = [i for i in range(10)]
# print(my_list)   

# my_list = [str(i) for i in range(10)]
# print(my_list)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# my_list = [random.randint(0,100) for _ in range(10)]
# print(my_list)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# my_list = [i**3 for i in range(10) if not i%2]
 
# print(my_list)

# +++++
# my_list = [(i, i**3) for i in range(10) if not i%2]
 
# print(my_list)

# ++++++++++++++++++++++++++++++++
my_set = {random.randint(0,10) for i in range(10)}

print(my_set)