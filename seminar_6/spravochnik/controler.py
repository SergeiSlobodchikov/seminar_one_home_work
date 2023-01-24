import  model
import  view
import time


def start():
    while (True):
        view.clear_screen()
        choice = view.main_menu()
        match choice:
            case "1":
                # вывод данных
                view.show_contacts(model.readFile())
            case "2":
                # добавление данных
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
            case "3":
                # поиск
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case "4":
                # удаление данных
                del_data()
            case "5":
                # Замена номера
                Change_contact()
            case "6":
                # выход
                exit(0)
            case _:
                print("неверный ввод")
                time.sleep(3)