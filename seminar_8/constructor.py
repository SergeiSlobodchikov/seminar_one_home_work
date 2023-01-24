import code_calculator as cc
import view_calculator as vc

def start():
  string = vc.menu_kalkulatora()
  my_list = cc.split_string(string)
  vc.otvet(cc.calculator(my_list))