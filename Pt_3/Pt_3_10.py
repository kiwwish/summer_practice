word = str(input("Введите строку: "))
word = word.lower()
word = word.replace(" ", "")
print({symbol: word.count(symbol) for symbol in word})
