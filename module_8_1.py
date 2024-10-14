def add_everything_up(num, string):
    try:
        return (num + string)
    except TypeError:
        return (str(num) + str(string))
    # return (num + string)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# 123.456строка
# яблоко4215
# 130.456