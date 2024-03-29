#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#Не учитывать знаки препинания и регистр символов. 
#За основу возьмите любую статью из википедии или из документации к языку.

text = """
Михаил Юрьевич Лермонтов – великий поэт и прозаик.Лермонтов родился в Москве 15 октября 1814 года,
ушел из жизни в результате дуэли 27 июля 1841 года в Пятигорске. Его творчество, 
сочетающее личные переживания, политические убеждения и философское мышление, 
повлияло на всю русскую литературу.
Тяжелое детство – ранняя смерть матери, напряженные отношения с жестокосердной бабушкой – оставили
отпечаток на характере, судьбе и творчестве Лермонтова. Традиционное для своего времени домашнее образование 
Михаил Лермонтов продолжил в благородном пансионе. Курс нравственно-политического отделения в университете
Москвы поэт не окончил. Лермонтов был намерен продолжить обучение в университете Петербурга, но не был зачислен. 
Поэтому он принял решение учиться в школе гвардейских юнкеров и по итогам обучения попал в статусе корнета 
в гусарский полк.
Творческий путь Лермонтова 
Первое произведение – поэма Хаджи Абрек – написано Лермонтовым в 1829 году,
но опубликовано было только спустя шесть лет. По весьма реалистичной легенде, рукопись выслали в редакцию 
без согласия автора. После первого литературного успеха Лермонтов создает около четырех сотен стихотворений,
несколько десятков поэм, знаменитые прозаические сочинения. Вспомним самые значительные произведения:
поэма Хаджи-Абрек, поэма Бородино, поэма Мцыри, поэма Герой нашего времени, поэма На смерть поэта, поэма Демон.
Превратности судьбы Лермонтова
Трагическая смерть Александра Пушкина взволновала Лермонтова. 
Так было рождено неугодное власти стихотворение На смерть поэта, которое повлекло ссылку поэта на Кавказ.
Там Лермонтов служил в звании прапорщика в Нижегородском драгунском полке. За возвращением в Петербург
в 1838 году последовала бескровная дуэль с де Барантом в 1940 году. Это снова провоцирует высылку поэта
на Кавказ, на этот раз в Тенгинский полк.
Лермонтов не вступал в брак и не имел детей. При этом все его творчество Лермонтова пронизано неистовым разочарованием 
в любви, вызванным разрушенными отношениями с Варварой Лопухиной. Она считается главным адресатом его
любовной лирики. Хотя столь же значительную роль в лирике сыграли отношения с Натальей Ивановой, 
которой Лермонтов посвятил цикл стихотворений, именуемый ивановским в литературоведческих кругах.
Считается, что чувства между поэтом и Натальей Ивановой были взаимными до некоторого переломного момента,
когда ему предпочли другого человека. Начиная с лета 1831 года тему предательства и неверности 
Лермонтов делает в любовной лирике ведущей. Творчество не раскрывает причин разочарования, но демонстрирует мучительные чувства лирического героя.
Последняя дуэль
Живя в Пятигорске, Лермонтов стремился выйти в отставку и посвятить остаток жизни литературному творчеству, 
хотя его бабушка не одобряла такого выбора. Встреча с однокашником, теперь майором в отставке Мартыновым
и пустая ссора поэта с ним оказались трагическими. Михаил Лермонтов погиб на дуэли.

"""

text = text.replace('.', '').replace(',', '').replace('!', '').replace('–', '').replace('?', '')\
.lower().split()

my_dict = {}

for item in text:
    my_dict.setdefault(text.count(item), set()).add(item)

pop_words = sorted(my_dict.items(), reverse=True)

coutn = 0
for key, value in pop_words:
    if coutn < 10:
        print(f'{key} раз встречается слово {value}')
        coutn += 1
