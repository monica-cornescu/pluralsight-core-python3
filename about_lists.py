""" learn more and practice with lists """

li = [-2, 0, 4, 7, -15, 15]
# negative indexing, works for strings and tuples as well
if li[-1] == 15 and li[-2] == -15:
    print("1. This is true!")

# slicing a list
if li[1:3] == [0, 4]:
    print("2. This is also true")

if li[1: -1] == [0, 4, 7, -15]:
    print("3. We've eliminated the first and the last element of the list")

if li[:3] + li[3:] == [-2, 0, 4, 7, -15, 15]:
    print("4. These are 2 halves of the list li")

# copy a list in order to create another list object but with the same content (same object references as the first list
# all these 3 are shallow copy
new_li = li[:]
if new_li is not li and new_li == li:
    print("5. These are two different lists with the same elements")

new_li_2 = li.copy()
if new_li_2 is not li and new_li_2 == li:
    print("6. new_li_2 is a shallow copy of li")

new_li_3 = list(li)
if new_li_3 is not li and new_li_3 == li:
    print("7. new_li_3 is a shallow copy of li")

# making a list with repetition, by multiplying an element, repeats the reference without copying the value
a_list = [[-1, 0]] * 9
a_list[5].append(1)
print("8. This adds 1 to all elements, since they refer to the same object, see?", a_list)

# other methods for lists
# find the location (index) of an element in a list; returns the first list element which is equal to the argument
w = "the quick fox jumps over the lazy dog".split()
print("9.", w, w.index("dog"), w.count("the"), "jumps" in w, "lazy" not in w)

# deleting an element, multiple methods
del w[6]
w.remove("quick")
print("10. Different methods for deleting an element from a list", w)

# inserting new elements by specifying the element and the index, or just the element
statement = "I accidentally the golden earrings".split()
statement.insert(2, "threw")
statement.append("to the garbage")
new_statement = statement + ["and", "I", "was", "very", "sad"]
print("11. New list after insert, append and add another list to it:   ", ' '.join(new_statement))

# reversing and sorting lists in place
li.reverse()
print(li)
li.sort()  # sorts ascending
print(li)
li.sort(reverse=True)   # actually sorts descending
print(li)

# sorting elements of a list by the length of each string element
weird_statement = "see Maria I dances do beautifully".split()
weird_statement.sort(key=len)
print("13. This statement is not weird anymore:   ", ' '.join(weird_statement))

# sorted() gives a new list, while reversed() can be used to create a new list
myli = [-17, 20, 14, 72, -15, 115]
so_myli = sorted(myli)
new_rev_myli = list(reversed(myli))
print(f"14. New lists are: so_li = {so_myli} and new_rev_li = {new_rev_myli} ", )


if __name__ == '__main__':
    print("This is all new stuff I've learned about lists")


