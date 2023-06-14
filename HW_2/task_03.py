#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.
import fractions
x = '1/3'
y = '1/2'

a, b = map(int, x.split('/'))
c, d = map(int, y.split('/'))


print(f'Сумма = {a * d + b * c}/{b * d}')
print(f'Произведение = {a * c}/{b * d}')


f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)
print(f1 + f2)
print(f1 * f2)
