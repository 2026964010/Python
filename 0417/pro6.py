def has_common(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False

list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]
print("list1=", list1)
print("list2=", list2)
print(has_common(list1, list2))