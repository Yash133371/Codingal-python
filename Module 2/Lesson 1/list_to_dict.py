def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = [item[1:]]
    return result
students = [
    [1, "John", 6],
    [2, "Jean", 5],
    [3, "Zack", 4]
]
print(students)
print(test(students))