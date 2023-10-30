from menu_function import * # Импортируем все функции из файла menu_function.py

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while (choice != 7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию абонента, телефон которого надо найти: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию абонента, у которого надо изменить телефон: ')
            new_number = input('Введите новый номер этого абонента: ')
            print(change_number('phonebook.txt', phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Введите фамилию абонента, которого надо удалить из справочника: ')
            print(delete_by_lastname('phonebook.txt', phone_book, last_name))
        elif choice == 5:
            putnumber = input('Введите номер телефона абонента, которого вы хотите узнать: ')
            print(find_by_number(phone_book, putnumber))
        elif choice == 6:
            user_data = input('Введите данные нового абонента через запятую (Фамилия,Имя,Телефон,Описание): ')
            add_user('phonebook.txt', phone_book, user_data)
        delete_empty_lines('phonebook.txt')
        phone_book = read_txt('phonebook.txt')
        choice = show_menu()