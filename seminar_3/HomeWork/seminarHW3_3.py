# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

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
            print(my_list)
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


def ThreeTaskV2():
    my_list1 = [round(random.uniform(0, 10), random.randint(0, 3)) for _ in range(10)]
    my_list = [my_list1[x]% 1 for x in range(len(my_list1)) if my_list1[x] != int(my_list1[x])]
    maximum = my_list[0]
    minimum = my_list[0]
    for i in range(len(my_list)):
        if maximum < my_list[i]:
            maximum = my_list[i]
        elif minimum > my_list[i]:
            minimum = my_list[i]
    difference = maximum - minimum
    print(f'{my_list1} \nmax {round(maximum, 3)} min {round(minimum, 3)} разница {round(difference, 3)}')
    
ThreeTaskV2()