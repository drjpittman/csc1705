
class_variable = 1

def begin():

    print("This is begin start...")

    def middle():
        print("This is middle in begin")
    
    middle()

    print("This is begin end...")
    return

def middle():
    def begin():
        print("This is the middle begin...")

    def middle():
        print("This is the middle in middle...")

    def end():
        print("This is the middle end")
    
    begin()
    middle()
    end()

def end():
    print("This is end start...")

    def begin():
        print("This is begin in end")

    def middle():
        print("This is middle in end")

    begin()
    middle()

    print("This is the end end")


begin()
middle()
end()