from return_data_file import data_file

def copy_data():
    data = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка, такой строки не существует!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    choise = int(input("Введите номер файла назначения: "))
    with open(f'db\data_{choise}.txt', 'a', encoding='utf-8') as destination:
        for number_row in data:
            destination.write(f'{number_row}')