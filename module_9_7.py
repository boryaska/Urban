def is_prime(func):

    def wrapper(*args):

        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
                return True 
            
        result = func(*args)
        print('Простое' if is_prime(result) else 'Составное')
        return result
    
    return wrapper

@is_prime
def sum_three(*numbers):
    res = sum(numbers)
    return res

result = sum_three(2, 3, 7)
print(result)