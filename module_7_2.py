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
    strings_positions = dict()
    file = open('test.txt', 'w', encoding='utf-8')
    num = 0

    for string in strings:
        num += 1
        strings_positions[(num, file.tell())] = string
        file.write(f'{string} + \n')

    for keys, values in enumerate(strings_positions.items(), 1):
        print(f'{keys} {values}')
        file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
