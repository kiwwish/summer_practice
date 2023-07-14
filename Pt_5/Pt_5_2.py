import csv
a = int(input("Сколько книг Вы хотите добавит в список? "))
with open("books.csv", "a") as file:
    for i in range(a):
        title_of_book = str(input("Введите название книги: "))
        author_of_book = str(input("Введите автора этой книги: "))
        year_of_book = str(input("Введите год издания книги: "))
        line = title_of_book + "," + author_of_book + "," + year_of_book + "\n"
        file.write(line)

with open("books.csv", "r") as file:
    check = str(input("Введите фамилию автора, чьи книги Вы хотите найти: "))
    count = 0
    print("По вашему запросу было найдено следующее: ")
    for el in file:
        if check in el:
            print(el.replace(";", ", "))
            count = count + 1
    if count == 0:
        print("Ничего не найдено")


