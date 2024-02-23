if condition:
    print("condition")
else:
    print(alternative)
age = int(input("How old are you? "))
if age >= 18:
    print("You are old enough to move out")
    print("You are old enough to have an ID")
else:
    print("you are young to move out")
    print("You are not valid for an ID")
Marks = int(input("Enter Marks"))
if Marks >= 80 and Marks <=100:
    print("A")
elif Marks >=60 and Marks <=79:
    print("B")
elif Marks >=50 and Marks <=59:
    print("C")
elif Marks >=40 and Marks <=49:
    print("D")
elif Marks >=0 and Marks <=39:
    print("E")
else:
    print("Enter valid Marks ")
age = int(input("How old are you? "))
if age >=65:
    print("You are old enough to retire")
elif age <65 and age >=50:
    print("You are almost going to retire")
elif age <50 and age >40:
    print("You are still active")
elif age <40 and age >=18:
    print("You are considered youthful")
else:
    print("You are still young")


# Create a program that takes in human temperature in celcius and performs certain tasks.
# If the temperature is above 30, tell the user to have a vest on, If between 20and 30,
# the user should put on a sweater and if below 20, the user should put on a jacket.


Temperature = int(input("What's your temperature? "))
if Temperature >30:
    print("Have a vest on")
elif Temperature <=30 and Temperature >=20:
    print("Put on a sweater")
elif Temperature <20:
    print("Put on a jacket")
else:
    print("Enter accurate value")


# Take in the height and weight of a person as inputs. Let the height be in meters and weight
# in kg. Perform BMI calculations using the two inputs above. Now create a conditional statement to
# categorize the person using his/her BMI as follows. If BMI is below 18 the display, you are
# underweight, if 18 to 25 display you are normal, if 25 to 30 display you are overweight and
# above 30 you are obese.


Height = float(input("Enter height in meters "))
Weight = float(input("Enter weight in kg "))
BMI = Weight/(Height**2)
if BMI <18:
    print(BMI)
    print("You are underweight")
elif BMI >=18 and BMI <25:
    print(BMI)
    print("You are normal")
elif BMI >=25 and BMI <30:
    print(BMI)
    print("You are overweight")
elif BMI >=30:
    print(BMI)
    print("You are obese")
else:
    print("Enter accurate values")
