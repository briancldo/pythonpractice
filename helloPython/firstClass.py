from firstModule import *

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

class Goat(Person):
    def getAge(self):
        print(self.age)

    def __iter__(self):
        self.n = 1
        self.max = max
        return self

    def __next__(self):
        x = self.n
        if x == max:
            raise StopIteration
        else:
            self.n += 1
            return x

#modularFunction()
#fun2()

#Before
f = open("story.txt")
print(f.read())
print("\n")
f.close()

#Appending a line
f = open("story.txt", "a")
f.write(" Not to mention he is now the GOAT.")
f.close()

f = open("story.txt")
print(f.read())
print("\n")
f.close()

#Writing to a clean file:
f = open("story.txt", "w")
f.write("Once upon a time, Brian Do pulled a smoove move and hit the game winner in game 7 of the 2024 NBA Finals.")
f.close()

f = open("story.txt")
print(f.read())
print("\n")
f.close()
