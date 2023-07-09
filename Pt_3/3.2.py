n = int(input("Введите число, до которого показать ряд Фибоначчи: "))
fib = lambda n, x=0, y=1: [x] + fib(n, y, x + y) if y <= n else [x]
print(fib(n))