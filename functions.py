print("This is my first function")
print("This is my first function")
print("This is my first function")

def karibu():
    print("This is my first function")
    print("This is my first function")
    print("This is my first function")
karibu()
karibu()
def my_function(name):
    print(name)
    print(name)
    print(name)
my_function("Hanifa")
my_function("Adan")
my_function("Mohammed")

def num(number):
    print(number)
    print(number)
    print(number)
num(2)
num(3)
num(7)
num(0)

def salutation(first_name):
    print("Hi, " + first_name + " Good Morning.")
salutation("Hope")
salutation("Angel")
salutation("Mark")

def miaka(age):
    print("Hello, you are " + str(age) + " years old.")
miaka(20)

def my_name(first_name, last_name):
    print(first_name + "" + last_name + " is the student.")
my_name("Hanifa"," Adan")

def sentence(first_name, last_name, age):
    print(first_name + "" + last_name  + "" + " is " +  str(age) + " years old.")
sentence("Hanifa ", "Adan", 20)

def employees(first_name, age):
    if age >=20:
        print(first_name + " you are " + str(age) + " years old.")
    elif age <20 and age >=15:
        print(first_name + " you are " + str(age) + " years old.")
    elif age <15 and age >=10:
        print(first_name + " you are " + str(age) + " years old.")
    else:
        print(first_name + " you are " + str(age) + " young.")
employees("Paul", 18)
employees("Ann", 10)
employees("Grace", 5)

def age_calculator(age):
    new_age = age + 10
    return new_age
print(age_calculator(18))


def marks_calculator(*subjects):
    total_marks = sum(subjects)
    return total_marks
print(marks_calculator(23,45,67))
print(marks_calculator(2,56,68,90))
print(marks_calculator(34,56))

# Create a function that takes three arguments. One is a string and two are integers:calculate
# the totals of the integers and display the output.

def test(marks, int1, int2):
    total = int1 + int2
    return total
print(test("Marks",20,30))
print(test("Marks",15,30))

# Create a function that takes in location and age arguments. Then perform conditional
# statements as follows: above 60 post them to Kisumu, 50-60 post them to Nakuru, 59-40
# post them to Mombasa. Others to be posted to Nairobi.


def placement(location, age):
    if age >60:
        print("Kisumu")
    elif age >=50 and age <=60:
        print("Nakuru")
    elif age >=40 and age <=59:
        print("Mombasa")
    else:
        print("Nairobi")
placement("", 18)
placement("", 70)
placement("", 40)
placement("", 50)

def country(nchi ="Kenya"):
    return nchi
print(country("Tanzania"))
print(country("Uganda"))
print(country("Russia"))
print(country("Ghana"))
