# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import random

def TwoTask():
    my_list = []
    my_list2 = []
    number = int(input('Введите размер списка '))
    for i in range(number):
        my_list.append(random.randint(0, 10))
    if number % 2 != 0:
        number += 1
    for i in range(number//2):
        my_list2.append(my_list[i] * my_list[-(i+1)])
    print(f'список {my_list}  \nпроизведение пар чисел {my_list2}')

# TwoTask()

def TwoTaskV2():
    my_list = [random.randint(0, 10) for _ in range(random.randint(5, 10))]
    print(f'список {my_list}') 
    expression = lambda x, y: x * y
    new_list = [expression(my_list[i], my_list[-(i+1)]) for i in range((len(my_list)+1)//2)]
    print(new_list)

TwoTaskV2()