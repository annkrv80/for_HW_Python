#Создайте функцию генератор чисел Фибоначчи

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
       
        
print(*fib(6))