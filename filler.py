import fitz  # PyMuPDF
import os
import shutil

with open('path.txt', 'r') as f:
    folder_name = f.read().strip()

#AMUR

# Путь к текстовому файлу с данными
data_file_path = os.path.join(folder_name, 'static', 'text.txt')  # Замените 'data.txt' на путь к вашему текстовому файлу с данными

# Путь к целевому PDF-файлу
target_pdf1_path = 'static/applications/Amur.pdf'  # Замените 'target.pdf' на путь к вашему целевому PDF-файлу

# Функция для заполнения данных в PDF по координатам
def fill_pdf_by_coordinates(data_file_path, target_pdf1_path):
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data_lines = data_file.readlines()

    pdf_document = fitz.open(target_pdf1_path)

    x_coords = [45, 45, 230, 355, 500, 400, 45, 45, 99999, 45, 230, 400, 500, 45, 99999, 45, 99999, 45, 400, 99999, 470, 400, 400, 99999, 99999, 99999, 320, 395, 300, 99999]  # Пример координат X
    y_coords = [150, 175, 175, 175, 175, 235, 330, 735, 99999, 355, 355, 355, 355, 415, 99999, 210, 99999, 385, 385, 99999, 735, 175, 210, 99999, 99999, 99999, 330, 330, 735, 99999]  # Пример координат Y


    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]


        for i, line in enumerate(data_lines):
            # Убедимся, что у нас есть достаточно координат
            if i >= len(x_coords) or i >= len(y_coords):
                break

            # Получаем текущие координаты
            x = x_coords[i]
            y = y_coords[i]


            page.insert_text((x, y), line.strip(), fontsize=12)

    # Сохраняем заполненный PDF-файл
    output_path = 'app Amur.pdf'  # Замените 'filled_target.pdf' на путь для сохранения заполненного PDF-файла
    pdf_document.save(output_path)


# Запуск функции для заполнения PDF по координатам
fill_pdf_by_coordinates(data_file_path, target_pdf1_path)

#PRIORITY

# Путь к текстовому файлу с данными
data_file_path = os.path.join(folder_name, 'static', 'text.txt')  # Замените 'data.txt' на путь к вашему текстовому файлу с данными

# Путь к целевому PDF-файлу
target_pdf2_path = 'static/applications/Priority.pdf'  # Замените 'target.pdf' на путь к вашему целевому PDF-файлу

# Функция для заполнения данных в PDF по координатам
def fill_pdf_by_coordinates(data_file_path, target_pdf2_path):
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data_lines = data_file.readlines()

    pdf_document = fitz.open(target_pdf2_path)

    x_coords = [130, 90, 360, 460, 500, 490, 100, 145, 360, 90, 270, 365, 380, 485, 99999, 110, 480, 99999, 360, 99999, 500, 99999, 130, 365, 99999, 99999, 345, 99999, 99999, 99999]  # Пример координат X
    y_coords = [100, 120, 120, 120, 120, 175, 155, 260, 728, 277, 277, 277, 277, 260, 99999, 175, 277, 99999, 155, 99999, 735, 99999, 140, 295, 99999, 99999, 260, 99999, 99999, 99999]  # Пример координат Y


    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]


        for i, line in enumerate(data_lines):
            # Убедимся, что у нас есть достаточно координат
            if i >= len(x_coords) or i >= len(y_coords):
                break

            # Получаем текущие координаты
            x = x_coords[i]
            y = y_coords[i]


            page.insert_text((x, y), line.strip(), fontsize=12)

    # Сохраняем заполненный PDF-файл
    output_path = 'app Priority.pdf'  # Замените 'filled_target.pdf' на путь для сохранения заполненного PDF-файла
    pdf_document.save(output_path)


# Запуск функции для заполнения PDF по координатам
fill_pdf_by_coordinates(data_file_path, target_pdf2_path)


#MITSU

# Путь к текстовому файлу с данными
data_file_path = os.path.join(folder_name, 'static', 'text.txt')  # Замените 'data.txt' на путь к вашему текстовому файлу с данными

# Путь к целевому PDF-файлу
target_pdf3_path = 'static/applications/Mitsu.pdf'  # Замените 'target.pdf' на путь к вашему целевому PDF-файлу

# Функция для заполнения данных в PDF по координатам
def fill_pdf_by_coordinates(data_file_path, target_pdf3_path):
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data_lines = data_file.readlines()

    pdf_document = fitz.open(target_pdf3_path)

    x_coords = [165, 100, 55, 180, 240, 220, 180, 100, 99999, 40, 200, 295, 340, 450, 99999, 70, 225, 99999, 360, 415, 200, 99999, 99999, 335, 99999, 99999, 100, 345, 99999, 105]  # Пример координат X
    y_coords = [137, 152, 165, 165, 165, 190, 290, 745, 99999, 305, 305, 305, 305, 290, 99999, 175, 315, 99999, 185, 315, 745, 99999, 99999, 315, 99999, 99999, 330, 330, 99999, 186]  # Пример координат Y


    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]


        for i, line in enumerate(data_lines):
            # Убедимся, что у нас есть достаточно координат
            if i >= len(x_coords) or i >= len(y_coords):
                break

            # Получаем текущие координаты
            x = x_coords[i]
            y = y_coords[i]


            page.insert_text((x, y), line.strip(), fontsize=11)

    # Сохраняем заполненный PDF-файл
    output_path = 'app Mitsu.pdf'  # Замените 'filled_target.pdf' на путь для сохранения заполненного PDF-файла
    pdf_document.save(output_path)


# Запуск функции для заполнения PDF по координатам
fill_pdf_by_coordinates(data_file_path, target_pdf3_path)


#CROSSROADS

# Путь к текстовому файлу с данными
data_file_path = os.path.join(folder_name, 'static', 'text.txt')  # Замените 'data.txt' на путь к вашему текстовому файлу с данными

# Путь к целевому PDF-файлу
target_pdf4_path = 'static/applications/Crossroads.pdf'  # Замените 'target.pdf' на путь к вашему целевому PDF-файлу

# Функция для заполнения данных в PDF по координатам
def fill_pdf_by_coordinates(data_file_path, target_pdf4_path):
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data_lines = data_file.readlines()

    pdf_document = fitz.open(target_pdf4_path)

    x_coords = [105, 115, 90, 255, 330, 420, 115, 87, 130, 115, 238, 305, 320, 90, 130, 450, 450, 335, 335, 330, 500, 99999, 130, 250, 99999, 99999, 270, 255, 340, 255]  # Пример координат X
    y_coords = [103, 117, 133, 133, 133, 97, 150, 255, 710, 287, 287, 287, 287, 165, 270, 111, 128, 270, 150, 255, 705, 99999, 180, 255, 99999, 99999, 270, 150, 705, 165]  # Пример координат Y


    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]


        for i, line in enumerate(data_lines):
            # Убедимся, что у нас есть достаточно координат
            if i >= len(x_coords) or i >= len(y_coords):
                break

            # Получаем текущие координаты
            x = x_coords[i]
            y = y_coords[i]


            page.insert_text((x, y), line.strip(), fontsize=8)

    # Сохраняем заполненный PDF-файл
    output_path = 'app Crossroads.pdf'  # Замените 'filled_target.pdf' на путь для сохранения заполненного PDF-файла
    pdf_document.save(output_path)


# Запуск функции для заполнения PDF по координатам
fill_pdf_by_coordinates(data_file_path, target_pdf4_path)



# DARLA
# Делим страницы
# Путь к исходному PDF-файлу
input_pdf_path = 'static/applications/Darla.pdf'

# Загружаем PDF-файл
pdf_document = fitz.open(input_pdf_path)

# Для каждой страницы создаем отдельный PDF-файл
for page_num in range(len(pdf_document)):
    new_pdf = fitz.open()
    new_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
    new_pdf.save(f'Darla page_{page_num + 1}.pdf')
    new_pdf.close()

pdf_document.close()

# Путь к текстовому файлу с данными
data_file_path = os.path.join(folder_name, 'static', 'text.txt')  # Замените 'data.txt' на путь к вашему текстовому файлу с данными

# Путь к целевому PDF-файлу
target_pdf5_path = 'Darla page_1.pdf'  # Замените 'target.pdf' на путь к вашему целевому PDF-файлу

# Функция для заполнения данных в PDF по координатам
def fill_pdf_by_coordinates(data_file_path, target_pdf5_path):
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data_lines = data_file.readlines()

    pdf_document = fitz.open(target_pdf5_path)

    x_coords = [50, 50, 315, 470, 520, 470, 99999, 99999, 99999, 50, 315, 470, 520, 99999, 99999, 450, 99999, 99999, 200, 99999, 99999, 99999, 50, 50, 50, 350, 410, 255, 99999, 99999]  # Пример координат X
    y_coords = [610, 675, 675, 675, 675, 610, 99999, 99999, 99999, 470, 470, 470, 470, 99999, 99999, 540, 99999, 99999, 540, 99999, 99999, 99999, 645, 505, 440, 440, 610, 610, 99999, 99999]  # Пример координат Y


    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]


        for i, line in enumerate(data_lines):
            # Убедимся, что у нас есть достаточно координат
            if i >= len(x_coords) or i >= len(y_coords):
                break

            # Получаем текущие координаты
            x = x_coords[i]
            y = y_coords[i]


            page.insert_text((x, y), line.strip(), fontsize=12)

    # Сохраняем заполненный PDF-файл
    output_path = 'app Darla page_1.pdf'  # Замените 'filled_target.pdf' на путь для сохранения заполненного PDF-файла
    pdf_document.save(output_path)


# Запуск функции для заполнения PDF по координатам
fill_pdf_by_coordinates(data_file_path, target_pdf5_path)


# Путь к текстовому файлу с данными
data_file_path = os.path.join(folder_name, 'static', 'text.txt')  # Замените 'data.txt' на путь к вашему текстовому файлу с данными

# Путь к целевому PDF-файлу
target_pdf6_path = 'Darla page_2.pdf'  # Замените 'target.pdf' на путь к вашему целевому PDF-файлу

# Функция для заполнения данных в PDF по координатам
def fill_pdf_by_coordinates(data_file_path, target_pdf6_path):
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data_lines = data_file.readlines()

    pdf_document = fitz.open(target_pdf6_path)

    x_coords = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 50, 99999, 99999, 99999, 99999, 50, 99999, 99999, 99999, 99999, 99999, 99999, 430, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]  # Пример координат X
    y_coords = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 740, 99999, 99999, 99999, 99999, 705, 99999, 99999, 99999, 99999, 99999, 99999, 740, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]  # Пример координат Y


    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]


        for i, line in enumerate(data_lines):
            # Убедимся, что у нас есть достаточно координат
            if i >= len(x_coords) or i >= len(y_coords):
                break

            # Получаем текущие координаты
            x = x_coords[i]
            y = y_coords[i]


            page.insert_text((x, y), line.strip(), fontsize=12)

    # Сохраняем заполненный PDF-файл
    output_path = 'app Darla page_2.pdf'  # Замените 'filled_target.pdf' на путь для сохранения заполненного PDF-файла
    pdf_document.save(output_path)


# Запуск функции для заполнения PDF по координатам
fill_pdf_by_coordinates(data_file_path, target_pdf6_path)


# Соединяем страницы
# Пути к двум PDF-файлам
pdf1_path = 'app Darla page_1.pdf'
pdf2_path = 'app Darla page_2.pdf'

# Создаем новый PDF-документ
merged_pdf = fitz.open()

# Открываем и добавляем первую страницу
pdf1 = fitz.open(pdf1_path)
merged_pdf.insert_pdf(pdf1)
pdf1.close()

# Открываем и добавляем вторую страницу
pdf2 = fitz.open(pdf2_path)
merged_pdf.insert_pdf(pdf2)
pdf2.close()

# Сохраняем объединенный PDF-файл
output_pdf_path = 'app Darla.pdf'
merged_pdf.save(output_pdf_path)
merged_pdf.close()

# Список имен PDF-файлов для удаления
pdf_files_to_delete = ['Darla page_1.pdf', 'Darla page_2.pdf', 'app Darla page_1.pdf', 'app Darla page_2.pdf']

# Получаем текущую директорию (корневую папку)
root_directory = os.getcwd()

# Удаляем каждый PDF-файл из списка
for pdf_file in pdf_files_to_delete:
    file_path = os.path.join(root_directory, pdf_file)
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f'Файл {pdf_file} не найден.')


# CEFI
# Делим страницы
# Путь к исходному PDF-файлу
input_pdf_path = 'static/applications/Cefi.pdf'

# Загружаем PDF-файл
pdf_document = fitz.open(input_pdf_path)

# Для каждой страницы создаем отдельный PDF-файл
for page_num in range(len(pdf_document)):
    new_pdf = fitz.open()
    new_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
    new_pdf.save(f'Cefi page_{page_num + 1}.pdf')
    new_pdf.close()

pdf_document.close()

# Путь к текстовому файлу с данными
data_file_path = os.path.join(folder_name, 'static', 'text.txt')  # Замените 'data.txt' на путь к вашему текстовому файлу с данными

# Путь к целевому PDF-файлу
target_pdf7_path = 'Cefi page_1.pdf'  # Замените 'target.pdf' на путь к вашему целевому PDF-файлу

# Функция для заполнения данных в PDF по координатам
def fill_pdf_by_coordinates(data_file_path, target_pdf7_path):
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data_lines = data_file.readlines()

    pdf_document = fitz.open(target_pdf7_path)

    x_coords = [80, 80, 75, 155, 228, 313, 315, 80, 280, 80, 315, 99999, 420, 420, 99999, 315, 315, 525, 315, 99999, 480, 99999, 99999, 315, 99999, 99999, 255, 315, 315, 311]  # Пример координат X
    y_coords = [152, 205, 240, 240, 240, 170, 223, 320, 660, 352, 352, 99999, 352, 320, 99999, 257, 152, 320, 273, 99999, 660, 99999, 99999, 337, 99999, 99999, 337, 240, 320, 205]  # Пример координат Y


    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]


        for i, line in enumerate(data_lines):
            # Убедимся, что у нас есть достаточно координат
            if i >= len(x_coords) or i >= len(y_coords):
                break

            # Получаем текущие координаты
            x = x_coords[i]
            y = y_coords[i]


            page.insert_text((x, y), line.strip(), fontsize=8)

    # Сохраняем заполненный PDF-файл
    output_path = 'app Cefi page_1.pdf'  # Замените 'filled_target.pdf' на путь для сохранения заполненного PDF-файла
    pdf_document.save(output_path)


# Запуск функции для заполнения PDF по координатам
fill_pdf_by_coordinates(data_file_path, target_pdf7_path)


# Путь к текстовому файлу с данными
data_file_path = os.path.join(folder_name, 'static', 'text.txt')  # Замените 'data.txt' на путь к вашему текстовому файлу с данными

# Путь к целевому PDF-файлу
target_pdf8_path = 'Cefi page_2.pdf'  # Замените 'target.pdf' на путь к вашему целевому PDF-файлу

# Функция для заполнения данных в PDF по координатам
def fill_pdf_by_coordinates(data_file_path, target_pdf8_path):
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data_lines = data_file.readlines()

    pdf_document = fitz.open(target_pdf8_path)

    x_coords = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]  # Пример координат X
    y_coords = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]  # Пример координат Y


    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]


        for i, line in enumerate(data_lines):
            # Убедимся, что у нас есть достаточно координат
            if i >= len(x_coords) or i >= len(y_coords):
                break

            # Получаем текущие координаты
            x = x_coords[i]
            y = y_coords[i]


            page.insert_text((x, y), line.strip(), fontsize=10)

    # Сохраняем заполненный PDF-файл
    output_path = 'app Cefi page_2.pdf'  # Замените 'filled_target.pdf' на путь для сохранения заполненного PDF-файла
    pdf_document.save(output_path)


# Запуск функции для заполнения PDF по координатам
fill_pdf_by_coordinates(data_file_path, target_pdf8_path)


# Соединяем страницы
# Пути к двум PDF-файлам
pdf1_path = 'app Cefi page_1.pdf'
pdf2_path = 'app Cefi page_2.pdf'

# Создаем новый PDF-документ
merged_pdf = fitz.open()

# Открываем и добавляем первую страницу
pdf1 = fitz.open(pdf1_path)
merged_pdf.insert_pdf(pdf1)
pdf1.close()

# Открываем и добавляем вторую страницу
pdf2 = fitz.open(pdf2_path)
merged_pdf.insert_pdf(pdf2)
pdf2.close()

# Сохраняем объединенный PDF-файл
output_pdf_path = 'app Cefi.pdf'
merged_pdf.save(output_pdf_path)
merged_pdf.close()

# Список имен PDF-файлов для удаления
pdf_files_to_delete = ['Cefi page_1.pdf', 'Cefi page_2.pdf', 'app Cefi page_1.pdf', 'app Cefi page_2.pdf']

# Получаем текущую директорию (корневую папку)
root_directory = os.getcwd()

# Удаляем каждый PDF-файл из списка
for pdf_file in pdf_files_to_delete:
    file_path = os.path.join(root_directory, pdf_file)
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f'Файл {pdf_file} не найден.')

# Путь к папке с PDF файлами
source_folder = "."

# Путь к файлу с текстом
text_file = os.path.join(folder_name, 'static', 'text.txt')

# Читаем первую строку из текстового файла
with open(text_file, 'r') as f:
    folder_name = f.readline().strip()

# Создаем папку с названием из первой строки текстового файла
target_folder = os.path.join(os.getcwd(), folder_name)
os.makedirs(target_folder, exist_ok=True)

file_names = ["app Amur.pdf", "app Cefi.pdf", "app Crossroads.pdf", "app Darla.pdf", "app Mitsu.pdf", "app Priority.pdf"]

# Перемещаем нужные PDF файлы в новую папку
for filename in os.listdir(source_folder):
    if filename in file_names:
        # Получаем имя файла без расширения
        base_name = os.path.splitext(filename)[0]
        # Создаем новое имя файла
        new_name = "app for {} {}".format(folder_name, base_name.split(' ')[1])
        # Добавляем расширение .pdf обратно к новому имени файла
        new_name += ".pdf"
        # Создаем пути для исходного и целевого файла
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, new_name)
        # Перемещаем и переименовываем файл
        shutil.move(source_path, target_path)
