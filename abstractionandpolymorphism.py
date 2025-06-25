class USA:
 def capital(self):
     print("Washington is capital")
 def language(self):
     print("English is mainly spoken")
 def type(self):
      print("It is developed")
class India:
 def capital(self):
     print("New delhi is capital")
 def language(self):
     print("Hindi is mainly spoken")
 def type(self):
     print("Developing country")
obj_ind = India ()
obj_us = USA ()
for country in (obj_us, obj_ind):
    country.capital()
    country.language()
    country.type()

from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can run and bark")
class Lion(Animal):
    def move(self):
        print("I can roar")

R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()



