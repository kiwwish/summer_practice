a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
if a>b:
    t=a
    a=b
    b=t
sum = 0
for i in range(a, b + 1):
    sum += i
print("Сумма чисел от А до В (включительно): ", sum)

