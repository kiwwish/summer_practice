a = int(input("Введите число: "))
check = lambda x: print("Оно чётное") if x % 2 == 0 else print("Оно не чётное")
print(check(a))
