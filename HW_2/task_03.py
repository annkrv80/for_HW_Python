#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.
import fractions
x = '1/3'
y = '1/2'

for i in x:
    for j in y:
        a = int(x[0])
        b = int(x[2])
        c = int(y[0])
        d = int(y[2])


print(f'Сумма = {a * d + b * c}/{b * d}')
print(f'Произведение = {a * c}/{b * d}')


f1 = fractions.Fraction(1, 3)
f2 = fractions.Fraction(1, 2)
print(f1 + f2)
print(f1 * f2)
