# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
# – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4
# (значения сгенерированы случайным образом 4 2 3 1 )
# Output: 9
import random 

def Randoms_massiv(from_num, to_num):
    n = int(input('Введите сколько кустов черники растет на круглой грядке '))
    massive = []
    for i in range(n):
        random_number = round(random.randint(from_num, to_num))
        massive.append(random_number)
    print(massive)
    return massive

max = 0
massiv = Randoms_massiv(1, 8)
grydka_1 = massiv[0]
grydka_2 = massiv[1]
grydka_3 = massiv[2]
for i in range(len(massiv)):
    if max < massiv[0] + massiv[1] + massiv[2]:
        max = massiv[0] + massiv[1] + massiv[2]
        grydka_1 = massiv[0]
        grydka_2 = massiv[1]
        grydka_3 = massiv[2]

    p = massiv.pop(0)
    massiv.append(p)

print(f'Максимальное число ягод собирающий модуль может собрать {max} кг за один заход.')
print(f'C главной грядки {grydka_2} кг и с соседних по {grydka_1} и {grydka_3} кг')