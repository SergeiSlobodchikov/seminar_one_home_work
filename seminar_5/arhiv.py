# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def Szhatie(text):
    text = [str(x) for x in text ]
    num = 1
    new_text = ''
    for i in range(1, len(text)):  # Считаем количество букв 
        if text[i-1] == text[i]: 
            num += 1 
        elif text[i-1] != text[i] and num > 1:
            new_text += (str(num) + text[i-1])
            num = 1  
        else:
            new_text += (str(num) + text[i-1])
        if i == len(text)-1:
                new_text += (str(num) + text[i])
    return new_text

def Rasarhiv(textA):
    textA = [str(x) for x in textA ]  
    new_text = ''
    multiply = 1
    for i in text:  # Ищем число 
        if type(i) == int: 
            multiply = int(i) 
        else: 
            new_text += (i * multiply)
    return new_text


# Открываем файл и читаем из него строку
with open(r'file.txt', 'r') as data:
    text = data.read()
print(f'Текст из файла file.txt {text}')
# Открываем файл и записываем в него сжатую строку
with open(r'textA.txt', 'w') as data:
    data.write(Szhatie(text))
# Открываем сжатый файл и читаем его
with open(r'textA.txt', 'r') as data:
    textA = data.read()
print(f'Текст из файла textA.txt {textA}')
# Открываем файл и записываем в него восстановленную строку
with open(r'file.txt', 'w') as data:
    data.write(Rasarhiv(textA))
