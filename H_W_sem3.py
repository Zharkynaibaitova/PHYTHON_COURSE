
# Встречаемость элемента в массиве

# list_1 = [1, 2, 3, 4, 5, 3, 3, 2]
# k = 3
# import random
# res = 0
# for i in range (len(list_1)):
#     if list_1[i] ==k:
#         res = res +1
# print (res)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8

# new_list = []

# for i in range(len(list_1)):
#     raznica = abs(list_1[i] - k)
#     new_list.append(raznica)


# min_value = new_list[0]
# for i in range(len(new_list)):
#     if new_list[i]<min_value:
#         min_value = new_list[i]
#         k = i

# print(list_1[k])
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# keys = {'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'}
# print(my_dict.fromkeys(keys, 'Пусто'))

# 'д', 'к', 'л', 'м', 'п', 'у' 
# 'б', 'г', 'ё', 'ь', 'я'
# 'й', 'ы'
# 'ж', 'з', 'х', 'ц', 'ч'
# 'ш', 'э', 'ю'
# 'ф', 'щ', 'ъ'

my_dict = {}
keys1 = {'д', 'к', 'л', 'м', 'п', 'у' }
keys2 = {'б', 'г', 'ё', 'ь', 'я'}
print(my_dict.fromkeys(keys1, 1)(keys2,2))
