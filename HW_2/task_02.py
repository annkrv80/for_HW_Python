#Напишите программу, которая получает целое число и 
#возвращает его шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A(10), B(11), C(12), D(13), E(14) и F(15).

num = int(input('Введите число: '))


def conver(num, system):
    result = list()
    while num > 0:
        if num % system == 10:
            result.append('a')
        elif num % system == 11:
            result.append('b')
        elif num % system == 12:
            result.append('c')
        elif num % system == 13:
            result.append('d')
        elif num % system == 14:
            result.append('e')
        elif num % system == 15:
            result.append('f')
        else:
            result.append(str(num % system))
        num = num // system
    result.reverse()
    return ''.join(result)


print(f"Число {num} в двоичной системе {hex(num)}")
print(conver(num, 16))
