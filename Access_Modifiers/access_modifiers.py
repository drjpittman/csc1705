#!/usr/bin/env python3
from snake import Snake

class AccessModifiers(Snake):

    def __init__(self, snake):
        self.x = snake._type_of_snake = "rattlesnake"
        #self.y = snake.getIsVenomous()

        self.z = snake.__isVenomous

        print(self.x)
        print(self.z)

snake = Snake("python", False)
a = AccessModifiers(snake)
