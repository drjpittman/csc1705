class Calculator:
    """a simple calculator class containing four arithmetic methods"""

    def subtract(self, x, y):
        """a method to subtract y from x"""
        return x - y

    def add(self, x, y):
        """a method to add x and y"""
        return x + y

    def divide(self, x, y):
        """a method to divide x by y"""
        return x / y

    def multiply(self, x, y):
        """a method to mutiply x and y"""
        return x * y


# the 'main' program is below 

calc = Calculator()

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4'):
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y, "=", calc.add(x, y))

        elif choice == '2':
            print(x, "-", y, "=", calc.subtract(y, x))

        elif choice == '3':
            print(x, "*", y, "=", calc.multiply(x, x))

        elif choice == '4':
            print(x, "/", y, "=", calc.divide(y, y))
        break
    else:
        print("Invalid Input")