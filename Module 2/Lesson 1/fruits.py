fruits = ["Apple", "Banana", "Mango"]
print(f"List: {fruits}")
print(f"Length of list: {len(fruits)}")
print(f"First item of list: {fruits[0]}")
print(f"Last item of list: {fruits[-1]}")

fruits.append("Guava")
print(f"Updated list: {fruits}")

fruits.remove("Mango")
print(f"Updated list: {fruits}")

fruits.sort()
print(f"Updated list: {fruits}")

fruits.pop(0)
print(f"Updated list: {fruits}")

print(f"Sliced list: {fruits[:1]}")
print(f"Multiplied list: {fruits * 2}")

fruits.clear()
print(f"Cleared list: {fruits}")