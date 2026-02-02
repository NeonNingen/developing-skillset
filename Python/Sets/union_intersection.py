day1_visitors = {'Alice', 'Bob', 'Charlie'}
day2_visitors = {'Charlie', 'David', 'Eva', 'Frank'}

# Union with |
union_result = day1_visitors | day2_visitors
print("Union using |: ", union_result)

# Union using union()
union_result_method = day1_visitors.union(day2_visitors)
print("Union using using union(): ", union_result_method)

# Intersection using &
print("Intersection using &", day1_visitors & day2_visitors)

# Intersection using intersection()
print("Intersection using intersection()", day1_visitors.intersection(day2_visitors))