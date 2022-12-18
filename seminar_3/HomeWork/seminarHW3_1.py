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

OneTask()