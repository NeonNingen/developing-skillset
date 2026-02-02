fruits = {'apple', 'banana', 'orange', 'grape'}

# conditional that checks if banana is in fruits (set)
if 'banana' in fruits:
    print("Yes, banana is in the set")
else:
    print("No, banana is not in the set")

set1 = {1, 2, 3, 4, 5}
numbers_to_check = {3, 6, 9}


# any function returns True if any element of the iterable is true
# x in y for x in z is a generator expression
result = any(num in set1 for num in numbers_to_check)

if result:
    print("At least one number from the list is present in the set")
else:
    print("None of the numbers from the list are in the set")


people = {'Alice': 25, 'Bob': 30, 'Charlie': 22}

# conditional that checks if Charlie (key) is in people (dict)
if 'Charlie' in people:
    print("Yes, Charlie is a key in dictionary")
else:
    print("No, Charlie is not a key in dictionary")