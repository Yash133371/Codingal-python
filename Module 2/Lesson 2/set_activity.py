my_set = {1, 2, 3, 4, 4, 4, 4}
print(my_set)
my_set.add(5)
print("Updated set:", my_set)

set1 = my_set
set2 = {2, 4, 4, 6}

print("\nSet 1:", set1)
print("Set 2:", set2)
print("Difference:", set1.difference(set2))
print("Symmetric difference:", set1.symmetric_difference(set2))