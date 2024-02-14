# Problem 4: Intersection of Two lists
list1 = [2, 4, 6, 8, 10, 12]
list2 = [3, 6, 9, 12, 15, 18]

intersect = list(filter(lambda x: x in list1, list2))
print(intersect)