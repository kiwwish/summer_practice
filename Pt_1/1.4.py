a = int(input("Введите число в диапазоне от 10 до 20: "))
while a<10 or a>20:
    if a<10:
        print ("Число меньше требуемого диапазона!")
        a = int(input("Повторите попытку: "))
    if a>20:
        print ("Число больше требуемого диапазона!")
        a= int(input("Повторите попытку: "))
print ("Спасибо!")

