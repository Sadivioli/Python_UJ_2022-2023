from functools import singledispatch, singledispatchmethod

@singledispatch
def fun(arg):
    print("Agrument może mieć jakikolwiek typ: "+ str(arg))

@fun.register(int)
def _(arg: int):
    print("Argument jest typu: " + str(type(arg)) + " " + str(arg))

@fun.register(list)
def _(arg: list):
    print("Argument jest typu: " + str(type(arg)) + " " + str(arg))

@fun.register(str)
def _(arg: str):
    print("Argument jest typu: " + str(type(arg)) + " " + str(arg))

class Splitter:
    @singledispatchmethod
    def split(self, arg):
        print("Nie mam funkcji do podzielenia tego argumentu: "+ str(arg))

    @split.register(str)
    def _(self, arg: int):
        #split string by letters
        splitted = [char for char in arg]
        print("Argument jest typu: " + str(type(arg)) + " " + str(splitted))
    
    @split.register(list)
    def _(self, arg: list):
        #split list by elements
        splitted = arg
        print("Argument jest typu: " + str(type(arg)) + " " + str(splitted))
    
    @split.register(int)
    def _(self, arg: int):
        #split int by digits
        splitted = []
        for i in range(len(str(arg))):
            splitted.append(int(str(arg)[i]))
        print("Argument jest typu: " + str(type(arg)) + " " + str(splitted))
    


def main():
    fun("Hello, world")
    fun(42)
    fun([1, 2, 3])
    splitter = Splitter()
    splitter.split("Hello, world")
    splitter.split(int(17))
    splitter.split([4, 5, 6])

main()


