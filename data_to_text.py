import os
from datetime import datetime

with open('path.txt', 'r') as f:
    folder_name = f.read().strip()

# Открываем файл для записи
with open(os.path.join(folder_name, 'static', 'text.txt'), 'w') as file:

    #СТРОКА 1
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 9

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 2
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 10

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 3
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 11

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 4
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 16

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 5
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 17

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 6
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 12

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 7
    # Указываем номера строк из другого файла, которые нужно взять в качестве строк
    line_number_1 = 1
    line_number_2 = 2

    # Читаем указанные строки из другого файла
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        # Записываем оба значения в новый файл
        file.write(lines[line_number_1 - 1].strip() + " " + lines[line_number_2 - 1].strip() + "\n")

    # СТРОКА 8
    # Указываем номера строк из другого файла, которые нужно взять в качестве строк
    line_number_1 = 1
    line_number_2 = 2

    # Читаем указанные строки из другого файла
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        # Записываем оба значения в новый файл
        file.write(lines[line_number_1 - 1].strip() + " " + lines[line_number_2 - 1].strip() + "\n")

    # СТРОКА 9
    # Указываем номера строк из другого файла, которые нужно взять в качестве строк
    line_number_1 = 1
    line_number_2 = 2

    # Читаем указанные строки из другого файла
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        # Записываем оба значения в новый файл
        file.write(lines[line_number_1 - 1].strip() + " " + lines[line_number_2 - 1].strip() + "\n")

    # СТРОКА 10
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 7

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 11
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 8

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 12
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 14

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 13
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 15

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 14
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 4

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 15
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 4

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 16
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 5

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 17
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 5

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 18
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 5

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 19
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 6

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 20
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 6

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 21


    # Получаем текущую дату и время
    current_date = datetime.now()

    # Преобразуем дату в строку в нужном формате
    date_string = current_date.strftime("%m/%d/%Y")

    # Записываем дату в файл
    file.write(date_string + "\n")

    # СТРОКА 22
    file.write("--\n")

    # СТРОКА 23
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 13

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 24
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 3

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 25
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 1

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 26
    # Указываем номер строки из другого файла, которую нужно взять в качестве строки
    line_number = 2

    # Читаем указанную строку из другого файла и записываем ее в новый файл
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
        lines = other_file.readlines()
        file.write(lines[line_number - 1])

    # СТРОКА 27
    file.write("100\n")

    # СТРОКА 28
    file.write("owner\n")

    # СТРОКА 29
    file.write("owner\n")

    # СТРОКА 30
    # Читаем строки с датами из файла
    with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as data_file:
        lines = data_file.readlines()
        # Парсим даты
        date_str_1 = lines[12].strip()
        # Выводим результат на экран

        # Получаем текущую дату и время
        current_date = datetime.now()

        # Преобразуем дату в строку в нужном формате
        date_str_2 = current_date.strftime("%m/%d/%Y")

        # Преобразуем строки в объекты datetime
        date_1 = datetime.strptime(date_str_1, '%m/%d/%Y')
        date_2 = datetime.strptime(date_str_2, '%m/%d/%Y')

        # Вычисляем разницу между датами
        delta = date_2 - date_1

        # Вычисляем количество лет и месяцев
        years = delta.days // 365
        months = (delta.days % 365) // 30
        # Выводим результат на экран

        result = f"{years}y{months}m"


        with open(os.path.join(folder_name, 'static', 'data.txt'), 'r') as other_file:
            file.write(f"{result}")




