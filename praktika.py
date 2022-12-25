# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите натуральное число '))
# numbers = 1
# while n <= 0:
#     n = int(input('Введите натуральное число '))
# if n == 0:
#     print('Вы ввели 0')
# else:
#     for i in range(n):
#         i = i + 1
#         numbers = i * numbers
#         print(f'{numbers}', end=' ')
# print()

# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# file = open('/Users/david/Desktop/python/homework/lesson2/task17.txt')
# positions = []
# for i in file.read():
#     if i.isdigit():
#         positions.append(int(i))


# Реализуйте алгоритм перемешивания списка.


# numbers = str(input('Введите: '))
# i = 0
# for char in numbers:
#     if char == '.':
#         i = 1
#     elif i == 1:
#         print(char)

# if i == 0:
#     print('целое число')
# my_lis =[1,2,3,4]
# x=4
# for i in my_lis:
#     x = x+1
#     my_lis.append(x)
#     print(i)
# x = 15.15467
# random.uniform(10.5, 25.5)
# x = x % 1
# print(x)
#
# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# list_2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# list_3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# list_4 = ["123", "234", 123, "567"]
# list_5 = []

# def proverka(my_list: list, search: str):
#     count = 0
#     index = 0
#     for string in my_list:
#         if string == search:
#             if count == 1:
#                 print(f'позиция второго вхождения {index}')
#                 break
#             count = 1
#         index += 1
#     else:
#         print('Нету второго вхождения -1')

# proverka(list_1,"qwe")
# proverka(list_2,"йцу")
# proverka(list_3,"йцу")
# proverka(list_4,"123")
# proverka(list_5,"123")

# print('Введите через пробел два натуральных числа сумму и произведение (двух чисел(X,Y≤1000))')
# s, p = [int(x) for x in input().split()]

# if s % 2 == 0 and p % 2 == 0:
#     shag = 2
# else:
#     shag = 1

# for x in range(0, s//2+1, shag):
#     print(x)
#     y = s-x
#     if p == x*y:
#         if x > 1000 or y > 1000:
#             print(f'Два числа которые загадал Петя {x} и {y}, но при этом они больше 1000, Петя нас обманул')
#             break
#         else:
#             print(f'Два числа которые загадал Петя {x} и {y} ')
#             break
# else:
#     print(f'Петя что напутал такой пары нет')

i = 4
if i / 2:
    print(i, 'чётное1')
else:
    print(i, 'нечётное1')
if i // 2:
    print(i, 'чётное2')
else:
    print(i, 'нечётное2')
if i % 2 == 0:
    print(i, 'чётное3')
else:
    print(i, 'нечётное3')
if i // 2 == 0:
    print(i, 'чётное4')
else:
    print(i, 'нечётное4')
if i % 2 != 0:
    print(i, 'нечётное5')
else:
    print(i, 'чётное5')
if i // 2 != 0:
    print(i, 'нечётное6')
else:
    print(i, 'чётное6')

# import random


# num1 = round(random.randint(1, 1000))
# num2 = round(random.randint(1, 1000))
# s = num1 + num2
# p = num1 * num2
# print(f"Петя загадал два числа вот их сумма {s} и произведение {p}")
# print("Катя перебором решила найти эти числа")
# x = 1
# hundred = 0
# fifty = 0
# ten = 0
# for i in range(0, s//2+1):
#     y = s-x
#     print(f"{x} x и {y} y")
#     if p == x*y:
#         print(f'Два числа которые загадал Петя {x} и {y} ')
#         break
#     if x * y < p and hundred != 1:
#                 x = x + 100
#                 if x * y > p:
#                     x = x - 100
#                     hundred = 1 
#     elif x * y < p and fifty != 1:
#                 x = x + 50
#                 if x * y > p:
#                     x = x - 50
#                     fifty = 1
#     elif x * y < p and ten != 1:
#                 x = x + 10
#                 if x * y > p:
#                     x = x - 10
#                     ten = 1
#     y = s-x
#     x += 1
    


# print( s)
