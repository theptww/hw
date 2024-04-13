menu = {1: 'Вывести полный справочник',
        2: 'Добавить телефон',
        3: 'Найти телефон/имя(имя/фамилия/номер)',
        4: 'Удалить контакт',
        5: 'Копировать контакт',
        0: 'Выйти из программы'}
inp = None

def add_number():
    name = input('Введите имя: ')
    name = name.capitalize()
    surname = input('Введите фамилию: ')
    surname = surname.capitalize()
    number = input('Введите номер телефона: ')
    with open('telephone.txt', 'a') as data:
        data.write(f'\n{name} {surname}: {number}')
    print(f'Контакт {name} {surname}: {number} сохранен')

def show_all():
    with open ('telephone.txt', 'r') as data:
        for i in data:
            if i == '\n':
                continue
            print(i)

def find():
    search = input('Введите имя/фамилию или телефон: ')
    search = search.capitalize()
    name_list = []
    found = False
    with open('telephone.txt', 'r') as data:
        for i in data:
            name_list = i.strip()
            if search in name_list:
                print(f'{i}\n')
                found = True
        if not found:
            print('Такого контакта нет\n')

def delete():
    inp = input('Чтобы показать все контакты нажмите Enter, либо наберите имя/фамилию или номер телефона контакта для удаления: ').capitalize()
    if inp == '':
        show_all()
        inp = input('Введите имя/фамилию или номер телефона контакта для удаления: ').capitalize()
    with open('telephone.txt', 'r') as data:
        index_to_delete = 0
        contact_list = []
        for i in data:
            contact_list.append(i)
        for name in range(len(contact_list)):
            if inp in contact_list[name]:
                index_to_delete = name
        if index_to_delete != 0:
            confirmation = input(f'Вы хотите удалить этот контакт: {contact_list[index_to_delete]} Enter - удалить. Если нет - нажмите на любую клавишу и Enter: ')
            if confirmation == '':
                contact_list.remove(contact_list[index_to_delete])
        else:
            print('Такого контакта нет\n')

    with open('telephone.txt', 'w') as data:
        for i in contact_list:
            data.write(i)

def copy():
    with open('telephone.txt', 'r') as data:
        cont = ''
        for i in data:
            cont += i
        cont = cont.split('\n')
        cont = set(cont)
        cont.remove('')
        cont = list(cont)
        count = 1
        for i in cont:
            print(f'{count}. {i}')
            count += 1
    with open('contacts.txt', 'a') as data:
        inp = int(input('Введите номер контакта, который хотите скопировать: '))
        data.write(f'\n{cont[inp - 1]}')
        print('Контакт скопирован в файл contacts.txt')


def main_menu(dict):
    global inp
    for key, value in dict.items():
        print(f"{key}. {value}")
    inp = int(input('Введите номер выбора: '))
    if inp == 1:
        show_all()
    if inp == 2:
        add_number()
    if inp == 3:
        find()
    if inp == 4:
        delete()
    if inp == 5:
        copy()

while inp != 0:
    input('Нажмите Enter чтобы начать/продолжить ')
    main_menu(menu)

