# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def OneTask():
    my_list = []
    number = int(input('Введите размер списка '))
    odd = 1
    summa = 0
    for i in range(number):
        my_list.append(random.randint(0, 10))
        if i == odd:
            summa += my_list[i]
            odd += 2

    print(f'{my_list} список \nСумма элементов нечетного индекса {summa} ')
# OneTask()


def OneTaskV2():
    my_list = [random.randint(0, 10) for _ in range(random.randint(5, 10))]
    print(f'список {my_list}')
    my_list = [my_list[x] for x in range(len(my_list)) if x % 2 != 0 ]
    while len(my_list) != 1:
        i = 1
        my_list[i-1] = my_list[i] + my_list[i-1]
        my_list.pop(i)
    print(f'Сумма элементов нечетного индекса {my_list[0]}')

def OneTaskV3():
    my_list = [random.randint(0, 10) for _ in range(random.randint(5, 10))]
    print(f'список {my_list}')
    my_list = list(filter(lambda x : x % 2 != 0, my_list))
    while len(my_list) != 1:
        i = 1
        my_list[i-1] = my_list[i] + my_list[i-1]
        my_list.pop(i)
    print(f'Сумма элементов нечетных чисел {my_list[0]}')

OneTaskV2()
OneTaskV3()

