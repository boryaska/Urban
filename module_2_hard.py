def get_result(n):
    dividers = []
    result = ''

    for i in range(3, n + 1):
        if n % i == 0:
            dividers.append(i)
    print(dividers)

    for i in dividers:
        a = 1
        b = i - 1
        
        while a < b:
            result += (str(a) + str(b))
            a += 1
            b -= 1

    print(result)        
            

get_result(19)