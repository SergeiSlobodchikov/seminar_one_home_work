import random
# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def OneTask():
    numbers = str(input('Введите число чтобы узнать сумму его цифр: '))
    summa = 0
    for char in numbers:
        if char.isdigit():
            summa += int(char)
    print(summa)


# 2 Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n=4 -> [2, 2.25, 2.37, 2.44]

def TwoTask():
    n = int(input(f'Введите количество чисел в списке последовательности (1 + 1/n)**n \n'
                  'количество: '))
    lst = [round((1+1/i)**i, 2) for i in range(1, n+1)]
    print(f'Список {lst}, сумма чисел из списка {round(sum(lst), 2)}')


# 3 Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум
# использование библиотеки Random для получения случайного int

def TreeTask():
    number = int(input('Задайте число для размера списка: '))
    spisok = []
    for i in range(number):
        spisok.append(random.randint(0, 100))
    print(spisok)
    spisok[::-1]
    
    for char in spisok*2:
        p = spisok.pop(random.randint(0, number-1))
        spisok.insert(random.randint(0, number-1), p)

    print(spisok)


# OneTask()
# TwoTask()
# TreeTask()