class dad:
    def __init__(self, eyes, aggressive):
        self.eyes = eyes
        self.aggressive = aggressive

    def display(self):
        print("Your eye color is", self.eyes)
        print("You are aggressive", self.aggressive)

class son(dad):
    def __init__(self, name, age, eyes, aggressive):
        self.name = name
        self.age = age
        super().__init__(eyes, aggressive)

obj = son("Penguin", 8, "blue", True)
obj.display()

class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)
a = Employee('Rahul', 886012, 200000, "Intern")
a.display() 

class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")
PEBsy = Penguin()
PEBsy.whoisThis()
PEBsy.swim()
PEBsy.run()

class Vehicle:
    def __init__(self, fare):
        self.fare = fare

    def monthlyfare(self, days):
        return self.fare* days

class Bus(Vehicle):
    def __init__(self):
        super().__init__(fare=50)
class Volvo(Vehicle):
    def __init__(self):
        super().__init__(fare=100)
bus = Bus()
volvo = Volvo()
bus_fare = bus.monthlyfare(30)
volvo_fare = volvo.monthlyfare(30)
print("Total fare for Bus in 1 month is Rs", bus_fare)
print("Total fare for Volvo in 1 month is Rs", volvo_fare)

