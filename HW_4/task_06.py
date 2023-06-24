# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
#до конца и/или начала списка.


numbers_list = [1, 2, 1, 4, -1, 5]
a = int(input('Введите нижнюю границу диапазона: '))
b = int(input('Введите верхнюю границу диапазона: '))
start = min(a, b)
finish = max(a, b)


if start < 0:
    print(numbers_list[:finish+1])
    result = sum(numbers_list[:finish+1])
elif finish > len(numbers_list):
    result = sum(numbers_list[start::])
elif start < 0 and finish > len(numbers_list):
    result = sum(numbers_list)
else:
    result = sum(numbers_list[start:finish+1])


print(f'Сумма = {result}')
