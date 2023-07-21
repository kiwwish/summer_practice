import csv


def books(first, last):
    books = []
    with open("books.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        for el in reader:
            for year in range(first, last + 1):
                year = str(year)
                if year == el["Год издания"]:
                    books.append(el)
    if not books:
        print("В списке ет книг этого временного промежутка")
    else:
        for el in books:
            print(el["Название книги"], " ", el["Автор"], " ",
                  el["Год издания"])


try:
    first_yr = int(input("Введите нижнюю границу диапазона годов: "))
    last_yr = int(input("Введите верхнюю границу диапазона годов: "))
    books(first_yr, last_yr)
except ValueError:
    print("Введено не число!")
