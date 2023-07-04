# Заменить максимальные оценки на минимальные и минимальные на максимальные

# import random

# def create_journal(objs: int) -> list[int]:
#     return [random.randint(1,5) for _ in range(objs)]

# def hack_journal(journal: list[int]) -> list[int]:
#     max_mark = max(journal)
#     min_mark = min(journal)
#     for i in range(len(journal)):
#         if journal[i] == max_mark:
#             journal[i] = min_mark
#     return journal

# my_j = create_journal(int(input('Введите количество оценок: ')))
# print(my_j)
# print(hack_journal(my_j))

   
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# number = int(input('Введите число: '))

# def is_simple(num: int) -> bool:
#     if num in [1,2]:
#         return True
#     if num%2 ==0:
#         return False
#     for i in range(3, num//2+1, 2):
#         if num%i == 0:
#             return False
#     return True
        
# print(is_simple(number))
# --------------------------------------------------------------------------------------

#  Только с помошью рекерсии. 
# Дано натуральное число N  и последовательность из N элементов
# Требуется вывести эту последовательность в обратном порядке

# def reverse_input(num: int) -> str:
#     if num == 0:
#         return ''
#     char = input('Введите что то: ')
#     return reverse_input(num-1) + char

# print(reverse_input(5))



