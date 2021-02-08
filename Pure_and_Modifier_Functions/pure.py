#!/usr/bin/env python3

class Snake:

    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        print("zzzzZzzzz")


def pure_function(string):  #take a string as parameter
    python = Snake(string)  #instantiate a Snake object and pass the string parameter as 'name'
    return python           #return the instantiated Snake object



my_snake = pure_function('Phil')
print(my_snake.name)