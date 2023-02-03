# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self,x):
        print("wykonanie foo: (" + str (self) + ", " + str (x) + ")")

    @classmethod
    def class_foo(cls,x):
        print("class_foo: (" + str (cls) + ", " + str (x) + ")")
    
    @staticmethod
    def static_foo(x):
        print("static_foo: (" + str (x) + ")")

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

print("\n")
# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is moving\n")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying\n")

c = Car()
c.move()

p = Plane()
p.move()

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

class myInt(object):
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        print("getter: ", str(self._x))
        return self._x

    @x.setter
    def x(self, value):
        print("setter: ", str(value))
        self._x = value

a = myInt()
a.x = 123
a.x = 457
a.x = 890
a.x = 111

print(a.x)
