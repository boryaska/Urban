class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy    

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        tupl = (self.x_distance, self.y_distance)
        return tupl    

    def voice(self):
        print(self.sound)        

p1 = Pegasus()

print(p1.get_pos())   

p1.move(10, 15)
print(p1.get_pos())

p1.move(-5, 20)
print(p1.get_pos())

p1.voice()