# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random

def Table():
    candies = 28
    while candies <= 28:
        candies = int(input('Введите число конфет на столе их должно быть больше 28: '))
    return candies

def Step(candies):
    take_candies = -1
    while 0 > take_candies or take_candies > 28:
        take_candies = int(input('За один ход можно забрать не более чем 28 конфет: '))
        if take_candies > candies:
            print('ты хотел взять больше чем есть')
            take_candies = candies
    candies = candies - take_candies
    return candies

def StepAI(candies):
    take_candies = -1
    while 0 > take_candies or take_candies > 28:     
        if 28 >= candies:
            take_candies = candies  
        elif candies > 56:
            take_candies = 28
        elif 56 >= candies > 29:
            take_candies = candies - 29
        elif candies <= 29:
            take_candies = random.randint(1, 28) 
    candies = candies - take_candies
    print(f'забрал AI {take_candies}')
    return candies

candies = Table()
hod = random.randint(0, 2)
while candies != 0:
    if hod == 0:
        candies = Step(candies)
        print(f'конфет {candies}')
        if candies == 0:
            print('победил человек')
            break
        candies = StepAI(candies)
        print(f'конфет {candies}')
        if candies == 0:
            print('победил Ai')
            break
    elif hod != 0: 
        candies = StepAI(candies)
        print(candies)
        if candies == 0:
            print('победил Ai')
            break
        candies = Step(candies)
        print(f'конфет {candies}')
        if candies == 0:
            print('победил человек')
            break
    



