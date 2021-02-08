#!/usr/bin/env python3

class Python:

    def __init__(self, name):
        self.name = name
    
    def sleep(self, isAwake="Friday"):
        if isAwake is "Friday":
            print("zzzzzzzZzzzz")
        else:
            print("It is bedtime " + self.name + ", little snek.")

python = Python("Phil")

#condition 1
#python.sleep()

#condition 2
python.sleep("Wednesday")