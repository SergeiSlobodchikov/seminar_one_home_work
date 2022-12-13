def is_digit(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def Number(text):
    number = input(f'{text}')
    while(not is_digit(number)):
        number = input('ОШИБКА. Попробуйте снова: ')
    return int(number)


def is_natural(text):
    number = input(f'{text}')
    while(not number.isdigit()):
        number = input('ОШИБКА. Попробуйте снова: ')
    return int(number)