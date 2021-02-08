#!/usr/bin/env python3

class Snake:

    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        return 0
        print("zzzzZzzzz")


def pure_function(string):  #take a string as parameter
    python = Snake(string)  #instantiate a Snake object and pass the string parameter as 'name'
    return python           #return the instantiated Snake object

def add_surname(python, surname):
    python.name = python.name + " " + surname
    #return python

my_pure_snake = pure_function('Phil')
print(my_pure_snake.name)

my_modfified_snake = pure_function('Peetie')
add_surname(my_modfified_snake, "Pythonic") #call the modifier function to add our suraname to Snake.name
print(my_modfified_snake.name)

my_pure_snake.sleep()