<<<<<<< HEAD
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a > b and a > c:
    print("Наибольшее число: ", a)
    if b > c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b > c and b > a:
    print("Наибольшее число: ", b)
    if c > a:
        print(b, c, a)
    else:
        print(b, a, c)
else:
    print("Наибольшее число: ", c)
    if b > a:
        print(c, b, a)
    else:
        print(c, a, b)
=======
a = int (input("Введите первое число: "))
b = int (input("Введите второе число: "))
c = int (input("Введите третье число: "))
if a > b and a > c:
    print ("Наибольшее число: ", a)
    if b > c:
        print (a,b,c)
    else:
        print(a,c,b)
elif b > c and b > a:
    print("Наибольшее число: ", b)
    if c > a:
        print (b,c,a)
    else:
        print (b,a,c)
else:
    print("Наибольшее число: ", c)
    if b > a:
        print (c,b,a)
    else:
        print (c,a,b)
>>>>>>> d55fe4008be2a103bf49a2111395892436f94b6e
