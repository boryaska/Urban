def personal_sum(numbers):
    result = 0
    incorrect_data = 0   
    try:
        for num in numbers:
            try:
                result += num
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {num}')
                incorrect_data += 1
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None                   
    return (result, incorrect_data)        


def calculate_average(numbers):
    try:
        summ = personal_sum(numbers)[0]
    except TypeError:
        return None    
    
    try:
        length = 0
        for i in numbers:
            if  isinstance(i,(int, float)):
                length += 1
        return summ/length
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
