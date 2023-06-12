#Напишите программу, которая получает целое число и 
#возвращает его шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A(10), B(11), C(12), D(13), E(14) и F(15).

num = int(input('Введите число: '))


def conver(num, system):
    result = list()
    while num > 0:
        hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c' , 'd', 'e', 'f']
        result.append(hex_list[num % system])
        num = num // system
    result.reverse()   
    return ''.join(result)
    


print(f"Число {num} в шестнадцатиричной системе {hex(num)}")
print(conver(num, 16))
