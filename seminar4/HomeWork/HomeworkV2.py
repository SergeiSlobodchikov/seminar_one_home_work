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
        return dictionary  # Создаем словарь для степеней многочлена

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
    return my_str   # Из словаря в строку для красивого оформления многочленов

def ReplacePolynomial(data):
    for line in data:
        stroka = line
    yravnenieOne = stroka.replace(' ','').replace('=0','').replace('+',' ').replace('-',' -').replace('x^',' .')
    my_list = yravnenieOne.split()
    data.close() 
    return my_list        

def OpenAndWriteFile(data):    
    polynomialOne = RandomPolynomial()
    data.write(StringBeautiful(polynomialOne))
    data.close() 
    return polynomialOne

def StrokavSlovar(my_list: list):
    polynomialOnev1 = {}
    tochka = 0
    num = ''
    peremennay = 0
    one = 0
    zero = 0
    count = 0
    for i in my_list:
        for j in i: 
            if j == '.':
                tochka = 1
            elif tochka == 1:
                num += str(j)
            elif j == 'x':
                one = 1

        if tochka == 0: 
            peremennay = i
        elif tochka == 1:
            polynomialOnev1[int(num)] = polynomialOnev1.get(int(num), 0) + int(peremennay)
            num = ''
            tochka = 0
        if  one == 1:
            peremennay = i.replace('x', '')
            polynomialOnev1[1] = polynomialOnev1.get(1, 0) + int(peremennay)
            one = 0
        if count == len(my_list)-1:
            peremennay = i
            polynomialOnev1[0] = polynomialOnev1.get(0, 0) + int(peremennay)
        count += 1
    return polynomialOnev1

data = open(r'C:\Users\Acer\Desktop\python\seminar4\HomeWork\polynomialOne.txt', 'w')
polynomialOne = OpenAndWriteFile(data)
data = open(r'C:\Users\Acer\Desktop\python\seminar4\HomeWork\polynomialTwo.txt', 'w')
polynomialTwo = OpenAndWriteFile(data)

print(f'Словарь первого многочлена \n{polynomialOne}\n')
print(f'Словарь второго многочлена \n{polynomialTwo}\n')

data = open(r'C:\Users\Acer\Desktop\python\seminar4\HomeWork\polynomialOne.txt', 'r')
my_list = ReplacePolynomial(data)
data = open(r'C:\Users\Acer\Desktop\python\seminar4\HomeWork\polynomialTwo.txt', 'r')
my_listTwo = ReplacePolynomial(data)

polynomialOnev2 = StrokavSlovar(my_list)
polynomialTwov2 = StrokavSlovar(my_listTwo)

print(f'Словарь первого многочлена из файла \n{polynomialOnev2}\n')
print(f'Словарь второго многочлена из файла \n{polynomialTwov2}\n')

polynomialThree = {}

if len(polynomialOnev2) >= len(polynomialTwov2): 
    for i in polynomialOnev2: 
        polynomialThree[i] = polynomialOnev2.get(i, 0) + polynomialTwov2.get(i, 0)
else:
    for i in polynomialTwov2: 
        polynomialThree[i] = polynomialOnev2.get(i, 0) + polynomialTwov2.get(i, 0)

print(f'Словарь сложения многочленов\n{polynomialThree}\n')
print(f'Запись сложения многочленов\n{StringBeautiful(polynomialThree)}')