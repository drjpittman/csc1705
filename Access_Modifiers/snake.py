from animal import Animal

class Snake(Animal):

    def __init__(self, type_of_snake, isVenomous=True):
        self._type_of_snake = type_of_snake #protected...within and by subclasses
        self.__isVenomous = isVenomous #private...within only

    
    def getIsVenomous(self):
        return self.__isVenomous