# 1. Create a class Person with below details.
# a. The class should have the following attributes:
# i. name (string)
# ii. age (integer)
# iii. gender (string)
# b. The class should have the following methods:
# i. __init__(): to initialize the attributes.
# ii. introduce(): to print a statement introducing the person.
class person:
    def __init__(self,name,age,gender):
        self._name=name
        self._age=age
        self._gender=gender
    def intro(self):
        print(f"hi my name is  {self._name} and age is {self._age} and  my gender {self._gender}")

a=person("debashree",18,"female")
a.intro()

#2 . Create a class BankAccount, and implement below details.
# a. The class should have the following attributes:
# i. account_number (string)
# ii. account_holder (string)
# iii. balance (float)
# b. The class should have the following methods:
# i. __init__(): to initialize the attributes.
# ii. deposit(): to add money to the balance.
# iii. withdraw(): to subtract money from the balance.
# iv. get_balance(): to return the current balance
class BankAccount:
    balance=0
    def __init__(self,account_number,account_holder):

        self._account_number=account_number
        self._account_holder=account_holder

    def deposit(self,amount):
        self.balance=self.balance + amount

    def withdraw(self,amount):
        self.balance=self.balance - amount
    
    def get_balance(self):
        print(f"your account balance is {self.balance}")

b=BankAccount(1,"name")
b.deposit(10000)
b.get_balance()
b.withdraw(500)
b.get_balance()

# 3. Create a class Circle, and implement below details.
# a. The class should have the following attributes:
# i. x and y: centre coordinates (x axis and y axis).
# ii. radius: the radius of the circle.
# b. The class should have the following methods:
# i. get_area(): calculate and return the area of circle
# ii. get_perimeter(): return the perimeter of circle
# iii. get_circumference(): return circumference of the circle.
from math import pi
class Circle:
    def __init__(self,x,y,radius):
        self._x=x
        self._y=y
        self._radius=radius
    def get_area(self):
        print(f"area of the circle is {pi*self._radius*self._radius}")
    def get_perimeter(self):
        print(f"perimeter  of the circle is {2*pi*self._radius}")

c=Circle(1,1,4)
c.get_area()
c.get_perimeter

