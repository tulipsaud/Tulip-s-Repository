class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1500)
c.sell()

class myClass:
    __privateVar = 27
    def __privMeth(self):
        print("I'm inside class myClass")
    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)
        print("Call private method" , myClass.__privMeth(self))
foo = myClass()
foo.hello()


