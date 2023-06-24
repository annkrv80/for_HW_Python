#Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
#оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

names = 'Petr'
a = 6
bs = 33
d = 44
str = 'Hello'
s = 4
new_dict = {}


def no_s():
   for key, value in globals().items():
       if key[-1] == 's' and len(key) != 1:
           globals()[key] = None
           new_dict[key[:-1]] = value


print(names)
no_s()
print(names)
print(f'Переменные c s на конце {new_dict}')




