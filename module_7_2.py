def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    i = 1
    dct = dict()
    for text in strings:
       n = file.tell()
       file.write(text + '\n')
       dct[(i, n)] = text
       i += 1
    file.close()   
    return dct

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
