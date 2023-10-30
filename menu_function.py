# Функция, выводящаяя меню:

def show_menu():
    print('Выберите номер пункта в меню:',
          '1. Распечатать телефонный справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в телефонный справочник',
          '7. Завершить работу', sep = '\n')
    choice = int(input())
    return choice

# Функция, считывающая в список словарей телефонную книгу из файла:

def read_txt(filename):
    phonebook = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open (filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phonebook.append(record)
    return phonebook

# Функция, которая удаляет пустые строки из справочника:
def delete_empty_lines(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = [line for line in f if line!="\n"]
    open(filename,'w').writelines(lines)

# choice == 1:
# Функция, распечатывающая справочник в консоль:
def print_result(phonebook):
    for i in phonebook:
        s = ''
        for (k, v) in i.items():
            s += v + ', '
        print(f'{s[:-2]}') #

# choice == 2:
# Функция, ищущая телефон абонента по фамилии:
def find_by_lastname(phonebook, lastname):
    for i in phonebook:
        if i['Фамилия'] == lastname:
            # Если необходимо вывести только фамилию и телефон:
            print(f"{i['Фамилия']} - {i['Телефон']}")
                
            # Если необходимо кроме телефона и фамилии вывести отальную информацию: 
            # s = ''
            # for (f, n) in i.items():
            #     s += n + ', '
            # print(f'{s[:-2]}\n')

# choice == 3:
# Функция, которая находит абонента по фамилии, меняет номер телефона у абонента и перезаписывает файл
def change_number(filename, phonebook, lastname, newnumber):
    for i in phonebook:
        if i['Фамилия'] == lastname:
            i['Телефон'] = newnumber
    with open(filename, 'w', encoding='utf-8') as phbo:
        for j in phonebook:
            s = ''
            for v in j.values():
                s += v+','
            phbo.write(f'{s[:-1]}')

# choice == 4:
# Функция, которая находит абонента, удаляет его и перезаписывает файл без него:
def delete_by_lastname(filename, phonebook, lastname):
    new_phonebook = [i for i in phonebook if lastname not in i['Фамилия']]
    with open(filename, 'w', encoding="utf-8") as phbo:
        for j in new_phonebook:
            s = ''
            for v in j.values():
                s += v+','
            phbo.write(f"{s[:-1]}")

# choice == 5:
# Функция, ищущая абонента по номеру телефона
def find_by_number(phonebook, number):
    for i in phonebook:
        if i['Телефон'] == number:
            # Если необходимо вывести только фамилию и телефон:
            # print(f"{i['Фамилия']} - {i['Телефон']}")
                
            # Если необходимо кроме телефона и фамилии вывести отальную информацию: 
            s = ''
            for (f, n) in i.items():
                s += n + ', '
            print(f'{s[:-2]}\n')

# choice == 6:
# Функция, которая добавляет нового абонента в справочник:
def add_user(filename, phonebook, userdata):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    newPerson = dict(zip(fields, userdata.split(',')))
    phonebook.append(newPerson)
    with open(filename, 'a', encoding='utf-8') as phbo:
        s = ''
        for v in newPerson.values():
            s += v+','
        phbo.write('\n')
        phbo.write(f'{s[:-1]}')