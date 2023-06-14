#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
#Достаточно вернуть один допустимый вариант.
#*Верните все возможные варианты комплектации рюкзака.


list_of_things = {'Палатка': 15, 'Фонарик': 0.5, 'Спички': 0.1, 'Спальник': 5,
                  'Ведро': 1, 'Посуда': 3, 'Аптечка': 1, 'Обувь': 2, 'Топор': 1, 
                  'Тушенка': 0.9, 'Соль': 0.1, 'Макароны': 2,'Одежда': 5, 'Термос': 2,
                  'Чай': 1, 'Гитара': 3, 'Картофель': 5, 'Помидоры': 3, 'Огурцы': 3, 'Нож': 0.2,
                  'Котелок': 2, 'Потоленца': 1, 'Тазик': 1, 'Веревка': 1, 'Шашлык': 5, 'Вода': 3,
                  'Коврик': 1, 'Горелка': 2}

BACKPACK_WEIGHT = 30
backpack = set()
current_weight = 0


for things, weight in list_of_things.items():
    if current_weight + weight <= BACKPACK_WEIGHT:
        backpack.add(things)
        current_weight += weight
print(f'Список вещей в рюкзаке {backpack} весом {current_weight} кг')




