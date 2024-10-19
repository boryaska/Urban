def all_variants(text):
    n = len(text)
    total = 2 ** n 
    for i in range(1, total):  
        res = ''
        for j in range(n):
            if (i >> j) & 1:
                res += text[j]
        yield res

a = all_variants("abc")
for i in a:
    print(i)        