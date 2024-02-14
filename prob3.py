# Problem 3: Find Macimum
from functools import reduce

list = [2, 4, 6, 8, 10, 3, 1, 9, 23]
max_find = lambda lst: reduce(lambda x, y: x if x > y else y, lst)
greater_num = max_find(list)
print(greater_num)
