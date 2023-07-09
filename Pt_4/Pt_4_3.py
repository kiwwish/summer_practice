a = int(input("Ведите число А: "))
b = int(input("Ведите число B: "))
if a > b:
    t = b
    b = a
    a = t
primes = [x for x in range(a, b+1) if not [n for n in range(2, x) if not x % n]]
print("Простые числа в диапозоне от А до В: ", primes)