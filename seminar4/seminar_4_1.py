'32*x**2 + 4*x - 6 = 0'
'3*x**2 - 15*x + 0 = 0'
yravnenie = '32*x**2 + 4*x - 6 = 0'.replace('**2','').replace('+',' ').replace('= 0','').replace('*','').replace('x','').replace('  ','').replace('- ','-')
print(yravnenie)
my_list = yravnenie.split()

print(my_list)
for i in range(len(my_list)): 
    my_list[i] = int(my_list[i])

print(my_list)

from math import sqrt


def roots_equ(a, b, c):
    d = b ** 2 - 4 * a * c
    x_1 = (-b - sqrt(d)) / (a * 2)
    print(f'({-b} - {sqrt(d)}) / {a} * 2')
    x_2 = (-b + sqrt(d)) / (a * 2)
    return d, x_1, x_2

print(roots_equ(my_list[0], my_list[1], my_list[2]))