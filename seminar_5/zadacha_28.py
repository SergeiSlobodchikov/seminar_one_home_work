# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.

def summa(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a
 
a, b = [int(x) for x in input(f'Введите через пробел два неотрицательных числа,\nчтобы узнать сумму: ', ).split()]
print(summa(a, b))