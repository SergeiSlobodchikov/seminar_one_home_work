# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def Exponentiation(a, b, exp):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        exp *= a
        if a ** abs(b) == exp:
            return 1/exp
        else:
            return Exponentiation(a, b, exp)
    else:
        exp *= a
        if a ** b == exp:
            return exp
        else:
            return Exponentiation(a, b, exp)
    
    
 
a, b = [int(x) for x in input(f'Введите через пробел два числа(A, B),\nчтобы узнать А в степени B: ', ).split()] 
exp = a
print(Exponentiation(a, b, exp)) 