class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):  # Inherits from Animal
    pass

class Cat:
    def speak(self):
        print("Meow")


# Common interface
for animal in (Cat(), Dog()):
    animal.speak()


class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")