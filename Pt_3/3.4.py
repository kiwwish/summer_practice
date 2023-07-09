from random import randint
from functools import reduce
list = [randint(-10, 10)for i in range(5)]
new_list = [x*x for x in list]
print (list)
print (new_list)