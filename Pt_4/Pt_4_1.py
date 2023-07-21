num = str(input("Введите число: "))
list = [int(x) for x in str(num)]
for i in range(len(list) - 1):
    for j in range(len(list) - i - 1):
        if list[j] < list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(int(''.join(str(i) for i in list)))
