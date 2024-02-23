from ClassObject import Employees

class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Receptionist(Employees):

    def __init__(self, name, salary,gender):
        super().__init__(name,salary)
        self.gender = gender

class Frontend_developer(Receptionist):
    def __init__(self, name, salary, gender, programming_language):
        super().__init__(name, salary,gender)
        self.programming_language = programming_language
obj1 = Receptionist("Susan", 20000, "Female")
Employees1 = Employees("Felix", 50000)
dev1 = Frontend_developer("Hanifa", 100000,"Female", "python")
print(Employees1.name)
print(obj1.name)
print(dev1.programming_language)






