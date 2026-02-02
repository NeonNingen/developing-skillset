mutable_set = {1, 2, 3}

# add and remove function that adds 4 to the set and removes 2
mutable_set.add(4)
mutable_set.remove(2)

print("Mutable Set: ", mutable_set)

try:
    # frozenset constructor creates an immutable set
    immutable_set = frozenset({1, 2, 3})
    immutable_set.add(4)
except:
    print("This is not possible as the set is frozen")