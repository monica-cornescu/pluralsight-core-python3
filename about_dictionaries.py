""" learn more and practice with dictionaries """
from pprint import pprint as pp


# create a dictionary from a list of tuples
names_and_ages = [("Marius", 42), ("Monica", 45), ("Roxana", 47), ("Alex", 18)]
dict_names_and_ages = dict(names_and_ages)

# create dictionary directly from keyword arguments passed to dict
greek_alphabet = dict(a="alpha", b="beta", g="gamma", d="delta")

# copying of dictionaries is shallow: only references to keys and values objects are cop
# copy with copy function, less used
d2 = dict_names_and_ages.copy()
if d2 is not dict_names_and_ages and d2 == dict_names_and_ages:
    print(
        f"These 2 dictionaries, d2={d2} and {dict_names_and_ages} have the same elements but are not the same object")

# copy with dict, more common
d3 = dict(dict_names_and_ages)
if d3 is not dict_names_and_ages and d3 == dict_names_and_ages:
    print(f"There s dictionaries, d3={d3} and {dict_names_and_ages} have the same elements but are not the same object")

# extend a dictionary with elements of another dictionary (add entries from one dictionary to another)
d4 = {"gmail": "https://mail.google.com/mail/", "yahoo": "https://mail.yahoo.com/", "linkedin": "https://www.linkedin.com/"}
d3.update(d4)

# update an element of a dictionary and add a new element in one step
dict_names_and_ages.update({"Marius": 43, "mami": 77, "mama-soacra": 71})

# retrieve values from dictionary; the dictionary is an iterable which yields the next key at each iteration and
# retrieves the values
for key in dict_names_and_ages:
    print(f"{key} -> {dict_names_and_ages[key]}")

# iterate over the values of a dictionary; doesn't return a copy of them
print("Printing only the values")
for age in dict_names_and_ages.values():
    print(age)

# similarly we can retrieve only the keys:
print("Printing only the keys")
for person in dict_names_and_ages.keys():
    print(person)

# iterating over items (key, value pairs as tuples) with tuple unpacking in a for loop
for person, age in dict_names_and_ages.items():
    print(f"{person} -> {age}")

# membership tests on dictionaries (in, not in) work only on keys!
if "Roxana" in dict_names_and_ages and "tati" not in dict_names_and_ages:
    print("yes, Roxana is a person in our dictionary, but tati is not")

# deleting elements from a dictionary is done by deleting the keys:
catalog = {"AlexU": [10, 7, 8], "StefaniaU": [5, 8], "CatalinP": [4, 7, 6, 8], "CristinaV": [8, 9, 10], "MariaD": [9, 10, 10, 10]}
print("Initial catalog:", catalog)
del catalog["CatalinP"]
print("catalog after deleting one pupil:", catalog)

# modify value of a key in a dictionary, cause values are mutable
catalog["StefaniaU"] += [8, 6]
print("Catalog after StefaniaU gets new grades:", catalog)

# add new elements to the dictionary; dictionaries are mutable:
catalog["IonelB"] = [7, 9]
print("Catalog after IonelB joins the class:", catalog)
# Use pprint to print the dictionary (it also sorts the keys)
pp(catalog)

if __name__ == "__main__":
    print(dict_names_and_ages)
    print(greek_alphabet)
    print(f"d3 after update is:", d3)
    print("Updated dict_names_and_ages looks like this:", dict_names_and_ages)
