s = str(input("Введите строку: "))
palindromes = [s[i:j + 1] for i in range(len(s)) for j in range(i, len(s))
               if s[i:j + 1] == s[j:i - 1:-1]]
print(palindromes)
