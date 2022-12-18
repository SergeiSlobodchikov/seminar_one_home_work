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

    print(f'{my_list} список \n Сумма элементов нечетного индекса {summa} ')
# OneTask()

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


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

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def ThreeTask():
    def ListRandomFloat():
        my_list = []
        for _ in range(10):
            amount = random.randint(0, 3)
            number = round(random.uniform(0, 10), amount)
            if number == int(number):
                my_list.append(int(number))
            else:
                my_list.append(number)
        return my_list                      # Создал массив и заполнил его случайными числами

    def ListFraction(my_list):
        my_list2 = []
        for i in my_list:
            if i != int(i):
                my_list2.append(i % 1)
        return my_list2                     # Создал второй массив, но в него сохранил только дроби чисел

    def MaxAndMin(my_list2):
        maximum = my_list2[0]
        minimum = my_list2[0]
        for i in range(len(my_list2)):
            if maximum < my_list2[i]:
                maximum = my_list2[i]
            elif minimum > my_list2[i]:
                minimum = my_list2[i]
        difference = maximum - minimum
        return maximum, minimum, difference     # Перебрал второй массив и нашел разницу между max и min
        

    randomList = ListRandomFloat()
    fraction = ListFraction(randomList)
    maximum, minimum, difference = MaxAndMin(fraction)
    print(f'{randomList} \nmax {round(maximum, 3)} min {round(minimum, 3)} разница {round(difference, 3)}')
# ThreeTask()

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def FourTask():
    number = int(input('Введите десятичное число'))
    numberD = ''
    while number > 0:
        numberD = str(number % 2) + numberD
        number = number // 2

    print(numberD)
# FourTask()

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def FiveTask():
    number = int(input())
    my_list = [1, 0, 1]
    my_list2 = [1, 0, 1]
    negafibonachy = (my_list2[0+1]+my_list[0+2])
    for i in range(number-1):
        my_list.append(my_list[i+1]+my_list[i+2])
        my_list2.append(my_list2[i+1]+my_list2[i+2])
    for i in range(number-1):
        negafibonachy = (my_list2[i+1]+my_list2[i+2])
        if not i % 2:
            negafibonachy = -negafibonachy
        my_list.insert(0, negafibonachy)
    print(my_list)

def FiveTaskVTwo():
    number = int(input())
    my_list = [0, 1]
    minus_list = [0, 1]
    for i in range(number-1):
        my_list.append(my_list[i]+my_list[i+1])
        minus_list.append(minus_list[i]+minus_list[i+1])


    for i in range(1, number+1): 
        if not i % 2:
            my_list.insert(0, -minus_list[i])
        else:
            my_list.insert(0, minus_list[i])
    print(my_list)

FiveTask()
FiveTaskVTwo()