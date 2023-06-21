#Функция получает на вход словарь с названием компании в качестве ключа
#и списком с доходами и расходами (3-10 чисел) в качестве значения.
#✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
#прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

company_dict = {'Aeroflot': [1_000, -15_000, 25_000], 'S7': [5_000, -10_000, 6_000, -4_000],
                'Pobeda': [3_000, 4_000, -2_000]}


if any(map(lambda x: sum(x[1]) < 0, company_dict.items())):
    print('Хотя бы одина компания убыточная')
else:
    print('Все компании приносят прибыль')