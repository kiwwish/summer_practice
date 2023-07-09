from random import randint
from functools import reduce
list = [randint(-10, 10)for i in range(5)]
list_avg = reduce((lambda x, y: x + y), list)/len(list)
print(list)
print("Среднее значение списка чисел: ", list_avg)