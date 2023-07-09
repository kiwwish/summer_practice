a = int(input("Введите число: "))
list =[]
s = 0
while a > 0:
    b = a % 10
    list.append(b)
    a = a // 10
    s = s + 1
for i in range(s - 1):
    for j in range(s - i - 1):
        if list[j] < list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(int(''.join(str(i) for i in list)))