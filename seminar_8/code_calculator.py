# Уровень 4:
# - Действия разделяются скобками
# (12 - 4) * 2

def split_string(stroka: str):
  string = stroka.replace(' ', '').replace('+', ' + ').replace('*-', ' * -').replace('/-', ' / -').replace('^-', ' ^ -').replace('-(', ' + -1 * (')
  string = string.replace('*', ' * ').replace('/', ' / ').replace(')-', ' ) + -').replace('(', ' ( ').replace(')', ' ) ').replace(')', ' ) ').replace('^', ' ^ ')
  number = '0123456789'
  for i in number:
    string = string.replace(f'{i}-', f'{i} + -')
  my_list = string.split()
  if my_list[0] == '-':
    my_list[0] = float(my_list[1])*(-1)
    my_list.pop(1)
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
      elif ch == '^':
          return a ** b

  def zero_test(m: list):
    result = 0
    popp = 0
    finish = len(m)
    for i in range(finish - popp):
      if m[i] == '^':
        if m[i-1] != ')':
          result = calc(float(m[i-1]) , float(m[i+1]), (m[i]))
          m[i-1] = result
          m.pop(i)
          m.pop(i)
          popp += 2
          break
    return m

  def one_test(m: list):
    start = 0
    finish = 0
    result = 0
    popp = 0
    finish_1 = 0
    for i in range(len(m)):
      if m[i] == '(':
        start = i+1
      elif m[i] == ')' and finish_1 == 0:
        finish = i-1
        finish_1 = 1
        break
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
        break
    m.pop(start-1)
    m.pop(finish-popp)
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

  for i in range(len(my_list)):
    zero_test(my_list)
  while  '(' in my_list:
    one_test(my_list)
  while '^' in my_list:
    zero_test(my_list)
  zero_test(my_list) 
  testTwo(my_list)
  testThree(my_list)
  return my_list

