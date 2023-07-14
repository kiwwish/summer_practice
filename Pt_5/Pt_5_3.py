import  csv

def check_year (sting):
    return 0

first = str(input())
last = str(input())
file = list(csv.reader(open("books.csv")))
books =[]
for el in file:
    books.append(el)
count = 0
for el in books:
    if first <= int(books[el][2]) and int(books[el][2]) <= last:
        print(books[el])
    count = count + 1
if count == 0:
    print("Книг в данном диапозоне не найдено")