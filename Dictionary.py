my_dictionary = {
    "Name": "Hanifa",
    "Gender": "Female",
    "Age": 20,
    "Marital Status": "Single",
}
print(my_dictionary)
print(my_dictionary["Marital Status"])
print(my_dictionary["Name"])
print(my_dictionary["Age"])
print(my_dictionary.get("Gender"))
my_dictionary["Marital Status"] = "Married"
print(my_dictionary)
my_dictionary["Age"] = 21
print(my_dictionary)
my_dictionary["Location"] = "Nairobi"
print(my_dictionary)
my_dictionary["Salary"] = 20000
print(my_dictionary)
my_dictionary1 = my_dictionary.copy()
print(my_dictionary1)
print(len(my_dictionary1))
print(len(my_dictionary))
my_dictionary.pop("Marital Status")
print(my_dictionary)
my_dictionary.pop("Name")
print(my_dictionary)
del my_dictionary["Gender"]
print(my_dictionary)
my_dictionary.clear()
print(my_dictionary)
del my_dictionary
print(my_dictionary1)
car = {
    "Model": "BMW",
    "Type": "M3",
    "License": "KPTQ234D",
    "Manufacture Date": 20/20/2024,
    "Owner": "Hanifa Adan",
}
print(car)
print(len(car))
car["Type"] = "X6"
print(car)
print(car["Model"])
print(car.get("Type"))
car["Seller"] = "Louis Loo"
print(car)
car["Prize"] = 10000000
print(car)
car.pop("Manufacture Date")
print(car)
car.pop("license")
print(car)
del car
print(car)


















