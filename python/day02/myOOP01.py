class Animal:
    def __init__(self):
        self.flagLife = True
        self.age = 1
    def getOlder(self):
        self.age+=1

class Human(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.name = "홍길동"
    
    

man = Human()
print(man.age)
print(man.flagLife)
print(man.name)