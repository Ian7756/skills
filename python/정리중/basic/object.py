class Animal:
    # 생성자 올시다
    def __init__(self):
        self.flagLife = True
        self.age = 1
    def getOlder(self):
        self.age+=1
        
class Human(Animal):
    def __init__(self):
        # 상속 개념
        Animal.__init__(self)
        self.name = "홍길동"     

dog = Animal()
print(dog.flagLife)
print(dog.age)


class Dog:
    def __init__(self):
        self.age = 1
        
class Bird:
    def __init__(self):
        self.fPower=0

# 이중 상속 뭔데.. ㅡㅡ;;
class GaeSae(Dog,Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)

gs = GaeSae()
print(gs.age)
print(gs.fPower)