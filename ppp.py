class fruits:
    def __init__(self, name, price, color):
        self.color = color
        self.name = name
        self.price = price

    def onyesha(self):
        print(f"my favorite fruit is {self.name}" f"it's price is {self.price}" f"it's colour is {self.color}")


myobj = fruits("Banana", 100, "Yellow")
myobj.onyesha()