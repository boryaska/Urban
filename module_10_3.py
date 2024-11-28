import threading
import random
from time import sleep           
            

class Bank():
    def __init__(self):
        self.balance = int()
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            val = random.randint(50, 500)
            self.balance += val
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {val}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            val = random.randint(50, 500)
            print(f'Запрос на {val}')
            if self.balance >= val:
                self.balance -= val
                print(f'Снятие: {val}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')    
                self.lock.acquire()

bk = Bank()        
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')