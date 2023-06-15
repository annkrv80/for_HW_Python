#Три друга взяли вещи в поход. Сформируйте
#словарь, где ключ — имя друга, а значение —
#кортеж вещей. Ответьте на вопросы:
#✔ Какие вещи взяли все три друга
#✔ Какие вещи уникальны, есть только у одного друга
#✔ Какие вещи есть у всех друзей кроме одного
#и имя того, у кого данная вещь отсутствует
#✔ Для решения используйте операции
#с множествами. Код должен расширяться
#на любое большее количество друзей.

list_of_things = {'Petr': ('палатка', 'спальник', 'котелок'), 'Ivan':('горелка', 'продукты', 'палатка'),\
                'Max': ('палатка', 'вода', 'спички', 'продукты')}



common_things = set(list_of_things['Petr']) & set(list_of_things['Max']) & set(list_of_things['Ivan'])
print(f'Все три друга взяли {common_things}')

unique_things = set() 
th = list()

for name, things_list in list_of_things.items():
    for things in things_list:
        th.append(things) 
for i in th:
    if th.count(i) == 1:
        unique_things.add(i)
print(f'Вещи, которые есть только у одного из друзей {unique_things}')
          
        



