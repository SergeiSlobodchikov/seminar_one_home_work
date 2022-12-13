# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
def TwoTask():
    number = int(input('Введите трехзначное число: '))
    while number < 100 or number > 999:
        print('Это не трехзначное число')
        number = int(input('Введите трехзначное число: '))
    result = number // 100 + number // 10 % 10 + number % 10
    print(f'Сумма цифр числа {number} = {result}')


# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
def FourTask():
    numbers = int(input('Введите количество журавликов '))
    boys = 0
    katya = 0
    if numbers % 2 == 0:
       katya = numbers//3 * 2
       boys = (numbers - katya) // 2
       print(f'Катя сделала {katya} штук, а Петя и Сережа по {boys}')
    elif numbers % 2 != 0:
        numbers = numbers - 1
        katya = numbers//3 * 2
        boys = (numbers - katya) // 2
        print(f'Катя сделала {katya} штук, а Петя и Сережа по {boys} и 1 журавлик им сделал учитель')
    else:
        print('Что вы ввели?')

# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
def SixTask():
    ticket_number = int(input('Введите номер билетика: '))
    while ticket_number < 100000 or ticket_number > 999999:
        print('Номер билетиков шестизначные. Вы ввели что-то другое')
        ticket_number =  int(input('Введите номер билетика: '))
    my_list = []
    for i in range(6):
        my_list.append(int(str(ticket_number)[i]))
    first_half = 0
    second_half = 0
    for i in range(6//2):
        first_half = first_half + my_list[i]
        second_half = second_half + my_list[i+3]
        if i == 6//2-1 and first_half == second_half:
            print('Счастливый билет')
        elif i == 6//2-1:
            print('Может повезет в следущий раз')

# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
def EightTask():
    choco_row = int(input('Ширина шоколадки: '))
    choco_col = int(input('Высота шоколадки: '))
    piece = int(input('Сколько отламываем: '))

    if piece < choco_col * choco_row and piece > 0:
        if piece == 1 and (piece == choco_col or piece == choco_row):
            print('Получится отломить')
        else:
            if not piece % choco_col or not piece % choco_row:
                print('Получится отломить')
            else:
                print('Не получится отломить')
    elif piece == choco_col * choco_row:
        print('У вас шоколадка состоит из этого количества долек')
    else:
        print('Что вы хотите отломить')


# TwoTask()
# FourTask()
# SixTask()
# EightTask()