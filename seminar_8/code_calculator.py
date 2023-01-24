# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15

# 1. Где операторы?
# 2. Где числовые значения?

# Уровень 1:
# - 1 действие
# - 2 аргумента

# Уровень 2:
# - Количество действие произвольное
# 12 + 15 - 4


# Уровень 3:
# - Действия имеют приоритет
# 12 - 4*2

# Уровень 4:
# - Действия разделяются скобками
# (12 - 4) * 2

def split_string(stroka: str):
  string = stroka.replace(' ', '').replace('+', ' + ').replace('*-', ' * -').replace('/-', ' / -').replace('*', ' * ').replace('/', ' / ').replace('(', '( ').replace(')', ' )')
  string = string.replace('1-', '1 + -').replace('2-', '2 + -').replace('3-', '3 + -').replace('4-', '4 + -').replace('5-', '5 + -')
  string = string.replace('6-', '6 + -').replace('7-', '7 + -').replace('8-', '8 + -').replace('9-', '9 + -').replace('0-', '0 + -')
  my_list = string.split()
  if my_list[0] == '-':
    my_list[0] = float(my_list[1])*(-1)
    my_list.pop(1)
  print(my_list)
  return my_list

def calculator(my_list: list):
  def calc (a, b, ch):
      if ch == '+':
          return a + b
      elif ch == '-':
          return a - b
      elif ch == '/':
          return a / b
      elif ch == '*':
          return a * b

  def one_test(m: list):
    start = 0
    finish = 0
    result = 0
    popp = 0
    for i in range(len(m)):
      if m[i] == '(':
        start = i+1
      elif m[i] == ')':
        finish = i-1
    for j in range(start+1, finish - popp, 2):
        for i in range(start+1, finish - popp, 2):
          if m[i] == '*' or m[i] == '/':
            result = calc(float(m[i-1]) , float(m[i+1]), (m[i]))
            m[i] = result
            a = i
            m.pop(a+1)
            m.pop(a-1)
            popp += 2
    for j in range(start+1, finish - popp, 2):  
        if j == start+1:
          result = float(m[j-1])
        result = calc(result , float(m[j+1]), (m[j]))
        m[j] = result
        a = j
        m.pop(a+1)
        m.pop(a-1)
        popp += 2
    m.pop(a)
    m.pop(a-2)
    return m

  def testTwo(m: list):
      i = 0
      finish = len(m)-1
      while '/' and '*' in m:
        if m[i+1] == '*' or m[i+1] == '/':
          result = calc(float(m[i]), float(m[i+2]), (m[i+1]))
          m[i] = result
          a = i
          m.pop(a+1)
          m.pop(a+1)
          finish -= 2
        if len(m) == 1 or i >= finish:
          return m
        if m[i+1] != '/' and m[i+1] != '*':
          i += 1
      
  def testThree(m: list):
    i = 0
    while len(m) != 1:
      result = calc(float(m[i]), float(m[i+2]), (m[i+1]))
      m[i] = result
      a = i
      m.pop(a+1)
      m.pop(a+1)
    return m

  while  '(' in my_list:
    one_test(my_list)  
  testTwo(my_list)
  testThree(my_list)
  return my_list

