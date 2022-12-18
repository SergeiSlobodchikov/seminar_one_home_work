# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def FourTask():
    number = int(input('Введите десятичное число '))
    numberD = ''
    while number > 0:
        numberD = str(number % 2) + numberD
        number = number // 2
    print(f'Его двоичное число: {numberD}')

FourTask()