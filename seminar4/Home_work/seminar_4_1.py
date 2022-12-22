# ; Задача 22:
# ; Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# ; Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# ; Пользователь вводит 2 числа.
# ; n - кол-во элементов первого набора.
# ; m - кол-во элементов второго набора.
# ; Значения генерируются случайным образом.

# ; Input: 11 6
# ; (значения сгенерированы случайным образом
# ; 2 4 6 8 10 12 10 8 6 4 2
# ; 3 6 9 12 15 18)

# ; Output: 11 6
# ; 6 12

import random

def Randoms_massiv(size_massiv, from_num, to_num):
    n = round(random.randint(5, size_massiv))
    massive = []
    for i in range(n):
        random_number = round(random.randint(from_num, to_num))
        massive.append(random_number)
    print(massive)
    return massive


def Zadacha_22():
    print('Выводится два рандомных массива целых чисел от 5 до 20 элементов')
    massiv_1 = Randoms_massiv(20, 1, 20)
    massiv_2 = Randoms_massiv(20, 1, 20)
    num_set = set()  
    massiv_3 = []
    for i in massiv_1: 
        for j in massiv_2: 
            if i == j: 
                num_set.add(i)
    if num_set == set(): 
        print('У двух массивов нету общих чисел')
    else: 
        for i in num_set: 
            massiv_3.append(i)
        massiv_3 = sorted(massiv_3)
        print('Здесь видим их общие числа по порядку')
        print(massiv_3)

Zadacha_22()