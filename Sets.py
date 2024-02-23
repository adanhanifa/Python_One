my_set = {122,234,3455,445,52}
print(my_set)
my_set.add(243)
print(my_set)
my_set.update([785,4569,1287,3602])
print(my_set)
my_set1 = my_set.copy()
print(my_set1)
print(len(my_set))
my_set.discard(234)
print(my_set)
my_set.clear()
print(my_set)
del my_set
print(my_set1)
print(max(my_set1))
print(min(my_set1))
print(sum(my_set1))
print(sum(my_set1)/len(my_set1))

Names = {"John", "Smith", "Andrew", "Peter"}
print(Names)
if "Andrew" in Names:
    print("Andrew is present in the school system")
else:
    print("Andrew is not [present in school system")
if "Hanifa" in Names:
    print("Hanifa is present in the school system")
else:
    print("Hanifa is not in the school system")
Parents = {"Marian", "Mohammed", "Adan", "Osman", "Ali"}
one_value = "Adan"
if one_value in Parents:
    output = one_value
    print(output)


# Create a set of integers and floats values
# Then perform conditional statements to check their presence in the set


values = 254, 569, 489, 101, 156.3, 459.0, 147.5
if 254 in values:
    print("Value present")
else:
    print("Value absent")
if 156.3 in values:
    print("Value present")
else:
    print("Value absent")
if 123 in values:
    print("Value present")
else:
    print("Value absent")

