import itertools
list = list(map(int, input("Введите числа: ").split()))
a = int(input("Введите число: "))
new_list = []
for i in range(1, len(list) + 1):
    for el in itertools.combinations(list, i):
        if sum(el) == a:
            new_list.append(sorted(el))
print(new_list)
