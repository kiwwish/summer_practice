sum = 0
tryagain = True
while tryagain is True:
    i = float(input("Введите отрицательное число: "))
    if i > 0:
        print("Вы ввели положительное число. "
              "Сумма ранее введенных отрицательных чисел равна ",
              round(sum, 2))
        tryagain = False
    else:
        sum = sum + i
        print("На данный момент сумма отрицательных чисер равна ",
              round(sum, 2))
        print()
