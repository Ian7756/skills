class Dog:
    def __init__(self):
        self.age = 1
        
class Bird:
    def __init__(self):
        self.fPower=0

class GaeSae(Dog,Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)

gs = GaeSae()
print(gs.age)
print(gs.fPower)
