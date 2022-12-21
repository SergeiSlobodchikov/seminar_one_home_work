# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.
# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7
import random

n = int(input('Введите длину массива: '))
x = int(input(f'Введите число, которое необходимо проверить '))
massiveA = []
for i in range(n):
    random_number = round(random.randint(1, 20))
    massiveA.append(random_number)
print(massiveA)

condition = True
min = x-1
max = x+1
off = 0
while condition: 
    if off == 0:
        for i in massiveA:
            if i == x:
                print(f'Ну то же самое число самое близкое')
                condition = False
                break
        else:
            off = 1
    big = 0     
    if off == 1:
        for i in massiveA:
            if i == min or i == max: 
                if i == min:
                    print(f'Самое близкое число {min}')
                    condition = False
                    break
                else: 
                    big = 1
        if big == 1:
            print(f'Самое близкое число {max}')
            condition = False
            break

        min -= 1
        max += 1



