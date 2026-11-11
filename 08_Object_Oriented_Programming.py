# 1. Multilevel Inheritance
class Vehicle:
    def show(self):
        print("Vehicle")

class Car(Vehicle):
    def car(self):
        print("Car")

class ElectricCar(Car):
    def electric(self):
        print("Electric Car")

a = ElectricCar()
a.show()
a.car()
a.electric()


# 2. Multiple Inheritance
class Teacher:
    def teach(self):
        print("Teaching")

class Researcher:
    def research(self):
        print("Researching")

class Professor(Teacher, Researcher):
    pass

a = Professor()
a.teach()
a.research()


# 3. Hierarchical Inheritance
class Shape:
    def show(self):
        print("Shape")

class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

class Triangle(Shape):
    pass

Circle().show()
Rectangle().show()
Triangle().show()


# 4. Method Overriding
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

Dog().sound()
Cat().sound()


# 5. Operator Overloading - Complex Numbers
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def show(self):
        print(self.r, "+", self.i, "i")

a = Complex(2, 3)
b = Complex(4, 5)
c = a + b
c.show()


# 6. Private Variable - Salary
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def show(self):
        print(self.__salary)

a = Employee(50000)
a.show()


# 7. ATM System Using Encapsulation
class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def withdraw(self, pin, amount):
        if pin != self.__pin:
            print("Wrong PIN")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful")

    def show_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Wrong PIN")

a = ATM(1234, 10000)
a.show_balance(1234)
a.withdraw(1234, 2000)
a.show_balance(1234)


# 8. Game Character Design
class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print("Attack")

class Warrior(Character):
    def attack(self):
        print(self.name, "Sword Attack")

class Mage(Character):
    def attack(self):
        print(self.name, "Magic Attack")

class Archer(Character):
    def attack(self):
        print(self.name, "Arrow Attack")

Warrior("Thor").attack()
Mage("Harry").attack()
Archer("Robin").attack()
