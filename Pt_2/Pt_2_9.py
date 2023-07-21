n = int(input("Введите число: "))
n = str(n)
arr_n = []
for i in n:
    arr_n.append(i)
print("Порядок максимальной цифры с начала числа ",
      arr_n.index(max(arr_n)) + 1)
arr_n.reverse()
print("Порядок максимальной цифры с конца числа ", arr_n.index(max(arr_n)) + 1)
