# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

from random import randint
def RandomPolynomial():
        dictionary = {}
        k = int(input('Введите число степени многочлена-> '))
        for i in range(k, -1, -1):
            dictionary[i] = randint(-100,100)
        return dictionary

def StringBeautiful(dictionary: dict):
    my_str = ''
    count = len(dictionary) - 1
    step = len(dictionary) - 1
    proverka = True

    while proverka:
        if dictionary[step] == 0:
            step -= 1
        elif dictionary[step] != 0:
            proverka = False

    for k,v in dictionary.items(): 
        if count == len(dictionary) - 1 and v < 0: 
            my_str += ' -'

        if k == 1:
            if v == 0: 
                my_str += ''
            elif v == 1:
                 my_str += 'x'
            else:
                my_str += f'{abs(v)}x' 
        elif k == 0:
            if v == 0: 
                my_str += ''
            else:
                my_str += f'{abs(v)}'            
        elif v == 0: 
            my_str += ''
        elif v == 1: 
            my_str += f'x^{k}'
        else: 
            my_str += f'{abs(v)}x^{k}'

        if count > 0 and count <= step:
            if dictionary[count - 1] == 0:
                my_str += ''
            elif dictionary[count - 1] > 0:
                my_str += ' + '
            elif dictionary[count - 1] < 0:
                my_str += ' - '

        count -= 1
    my_str += f' = 0'
    return my_str  
        


polynomialOne = RandomPolynomial()
print(f'Первый многочлен\n{StringBeautiful(polynomialOne)}')
polynomialTwo = RandomPolynomial()
print(f'Второй многочлен\n{StringBeautiful(polynomialTwo)}')
polynomialThree = {}

if len(polynomialOne) >= len(polynomialTwo): 
    for i in polynomialOne: 
        polynomialThree[i] = polynomialOne.get(i, 0) + polynomialTwo.get(i, 0)
else:
    for i in polynomialTwo: 
        polynomialThree[i] = polynomialOne.get(i, 0) + polynomialTwo.get(i, 0)

print(f'Запись сложения многочленов\n{StringBeautiful(polynomialThree)}')