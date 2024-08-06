# Задача "Записать и запомнить":

# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название
# файла для записи, strings - список строк для записи.

# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell()
# перед записью.

# Примечания:
# Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# Не забывайте закрывать файл вызывая метод close() у объектов файла.
# Помните, что при использовании символов не принадлежащих таблице ASCII, вы используете больше байт для
# записи символа. Соответственно для чтения и записи информации из/в файл(-f)
# потребуется другая кодировка - utf-8.

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = dict()

    for key, value in enumerate(strings, 1):
        keys = (key, file.tell())
        strings_positions[keys] = value
        file.write(f'{value}\n')
    file.close()
    return strings_positions


if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


# def custom_write(file_name, strings):
#     file = open(file_name, 'w', encoding='utf-8')
#     strings_positions = {}
#
#     for string in strings:
#         file.write(string + '\n')
#         strings_positions[len(strings_positions) + 1, file.tell()] = string
#     file.close()
#     return strings_positions
#
# if __name__ == '__main__':
#
#     info = [
#         'Text for tell.',
#         'Используйте кодировку utf-8.',
#         'Because there are 2 languages!',
#         'Спасибо!'
#         ]
#     result = custom_write('test.txt', info)
#     for elem in result.items():
#         print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')
