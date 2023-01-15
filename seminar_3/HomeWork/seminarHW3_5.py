# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def FiveTask():
    number = int(input(f'Задайте число для создания списка Негафибоначчи:\n'))
    my_list = [0, 1]
    minus_list = [0, 1]
    for i in range(number-1):
        my_list.append(my_list[i] + my_list[i+1])
        minus_list.append(minus_list[i] + minus_list[i+1])
        

    for i in range(1, number+1): 
        if not i % 2:
            my_list.insert(0, -minus_list[i])
        else:
            my_list.insert(0, minus_list[i])
    print(my_list)

FiveTask()
