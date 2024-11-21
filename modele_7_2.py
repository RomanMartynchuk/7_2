def custom_write(file_name, strings):
    text = open(file_name, 'w')
    strings_positions = {}
    line = []
    for i in strings:
        buy_numbers = text.tell()
        text.write(f'{i}\n')
        line.append(i)
        strings_positions[len(line),buy_numbers] = i
    text.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)