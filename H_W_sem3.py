
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

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)
