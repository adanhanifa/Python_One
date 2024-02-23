class Person:
    name = "John"
    age = 18
    gender = "Male"
    marital_status = "Married"
print(Person.name)
print(Person.age)
print(Person.marital_status)
print(Person.gender)
Person.age = 20
print(Person.age)
class Employees:
    first_name = "Job"
    last_name = "Stone"
    Salary = 100000
    gender = ("Male")
    age = 33
    marital_status = "Married"
print(f"{Employees.first_name} {Employees.last_name} your age is {Employees.age} and earn a salary of {Employees.Salary} and you are a {Employees.gender}.")
print(f"{Employees.last_name} you are a {Employees.gender} who earns a salary monthly of {Employees.Salary}")
print(f"{Employees.first_name} is a {Employees.gender} of age {Employees.age}")
class Parent:
    first_name = "Esther"
    last_name = "Kiprop"
Parent1 = Parent()
print(Parent1.first_name)
print(Parent1.last_name)

class Parent:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
Parent1 = (Parent("Hanifa", "Adan",20 ))
Parent2 = (Parent("John", "Kitui", 26))
Parent3 = (Parent("Paul", "Chola", 18))
print(Parent1.first_name)
print(Parent2.first_name)
print(Parent3.first_name)
print(Parent1.last_name)
print(Parent2.last_name)
print(Parent3.last_name)
print(Parent1.age)
print(Parent2.age)
print(Parent3.age)

class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
Car1 = (Cars("Ford", "Ranger",2000))
Car2 = (Cars("Toyota", "Axis",2014))
Car3 = (Cars("Nissan", "Sunny",1999))
print(Car1.make)
print(Car1.model)
print(Car1.year)
print(Car2.make)
print(Car2.model)
print(Car2.year)
print(Car3.make)
print(Car3.model)
print(Car3.year)
print(f"My car model is {Car1.make} {Car1.model} manufactured in the year {Car1.year}")
print(f"{Car1.make},{Car2.make} and {Car3.make} are all manufactured in the year {Car3.year}")

# Create a class of students with three properties and derive three objects from it. Then
# display a  paragraph.

class Students:
    def __init__(self,first_name,last_name,grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
Student1 = Students("Jane", "Wambui", "A")
Student2 = Students("Jacob", "Otieno", "D")
Student3 = Students("Mary", "Kamau", "B")
print(Student1.first_name)
print(Student1.last_name)
print(Student1.grade)
print(Student2.first_name)
print(Student2.last_name)
print(Student2.grade)
print(Student3.first_name)
print(Student3.last_name)
print(Student3.grade)

print(f"{Student1.first_name} {Student1.last_name} is and excellent student, "
      f"she got an {Student1.grade}.{Student2.first_name} {Student2.last_name} "
      f"needs to pull up his socks, he score a {Student2.grade}.{Student3.first_name} "
      f"{Student3.last_name} is performing averagely, she got a {Student3.grade}.")

class Magari:
    def __init__(self, make, model, price, year):
        self.make = make
        self.model = model
        self.price = price
        self.year = year

    def describe(self):
        print(f"My favourite car is the {self.make} model {self.model} and it costs roughly ksh.{self.price}")
gari1 = Magari("Ford ", "Everest ", 16000000 ,2019)
gari2 = Magari("Mercedes ", "AMG ", 21000000 ,2022)
gari3 = Magari("BMW ", "X6 ", 20000000 ,2024)
gari1.describe()
gari2.describe()
gari3.describe()

class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def fullname(self):
        print(f"{self.first_name} {self.last_name}")

    def age(self):
        print(f"{self.age}")

    def gender(self):
        print(f"{self.gender}")

    def increment_age(self):
        self.age += 10
person1 = Person("Paul","Chola","Male",18)
person2 = Person("Hanifa","Adan","Female",20)
person3 = Person("Crystal","Shayla","Female",17)
print(person1.fullname())
print(person3.gender)
print(person1.age)
person1.increment_age()
print(person1.age)
