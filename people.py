class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def onyesha(self):
        print(f"My name is {self.name} and I am {self.age} years")


myobj = People("John", 29)
myobj.onyesha()
myobj = People("Leshan", 34)
myobj.onyesha()
myobj = People("Thuo", 24)
myobj.onyesha()
myobj = People("Scoppy", 17)
myobj.onyesha()
myobj = People("Baraka", 13)
myobj.onyesha()
