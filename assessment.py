# Define a python function student().Using function attributes display the names of all
# arguments.


def Students(name):
   print(name)
   print(name)
   print(name)
Students("Hanifa")
Students("Chola")
Students("Tabbie")


# Write a python class named Student with two attributes student_name, marks. Modify the
# attributes values of the said class and print the original and modified values of the
# said attributes.


class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def student_name(self):
        print(f"{self.student_name}")

    def marks(self):
        print(f"{self.marks}")

    def increment_marks(self):
       self.marks +=15
Student1 = Student("Hanifa", 430)
print(Student1.student_name)
print(Student1.marks)
Student2 = Student("Hope", 380)
print(Student2.student_name)
print(Student2.marks)
Student3 = Student("John", 410)
print(Student3.student_name)
print(Student3.marks)
Student1.increment_marks()
print(Student1.student_name)
print(Student1.marks)
Student2.increment_marks()
print(Student2.student_name)
print(Student2.marks)
Student3.increment_marks()
print(Student3.student_name)
print(Student3.marks)


# Write a python class named Rectangle constructed from length and width and a method that
# will compute the area of a rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width

Rectangle1 = Rectangle(30,10)
print(Rectangle1.length)
print(Rectangle1.width)
print(Rectangle1.calculate_area())
Rectangle2 = Rectangle(20,15)
print(Rectangle2.length)
print(Rectangle2.width)
print(Rectangle2.calculate_area())
Rectangle3 = Rectangle(60,20)
print(Rectangle3.length)
print(Rectangle3.width)
print(Rectangle3.calculate_area())


# Write a python class named circle constructed from a radius and two methods that will
# compute the area and perimeter of a circle.


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
Circle1 = Circle(14)
print(Circle1.radius)
print(Circle1.calculate_area())
print(Circle1.calculate_perimeter())
Circle2 = Circle(35)
print(Circle2.radius)
print(Circle2.calculate_area())
print(Circle2.calculate_perimeter())
Circle3 = Circle(7)
print(Circle3.radius)
print(Circle3.calculate_area())
print(Circle3.calculate_perimeter())


# Write a python class BankAccount with attributes like account_number,
# balance, date_of_opening and customer_name and methods like deposit,
# withdraw and check_balance.


import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, opening_balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = opening_balance
        self.date_of_opening = datetime.datetime.now()

    def deposit(self, amount,):
        if amount >0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 <amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def check_balance(self):
        return self.balance

account1 = BankAccount(1245872,"Hanifa", 10000)
print(account1.account_number)
print(account1.customer_name)
print(account1.date_of_opening.strftime("%Y-%m-%d"))
print(account1.check_balance())
account1.deposit(500)
print(account1.check_balance())
account1.withdraw(200)
print(account1.check_balance())
account2 = BankAccount(8594714,"Paul", 24000)
print(account2.account_number)
print(account2.customer_name)
print(account2.date_of_opening.strftime("%Y-%m-%d"))
print(account2.check_balance())
account2.deposit(1000)
print(account2.check_balance())
account2.withdraw(800)
print(account2.check_balance())
account3 = BankAccount(5489214,"Tabbie", 50000)
print(account3.account_number)
print(account3.customer_name)
print(account3.date_of_opening.strftime("%Y-%m-%d"))
print(account3.check_balance())
account3.deposit(700)
print(account3.check_balance())
account3.withdraw(150)
print(account3.check_balance())




