#Нарисовать в консоли ёлку спросив
#у пользователя количество рядов.

SPASE = ' '
STAR = '*'
rows = int(input('Сколько рядов у елки? '))
spases = rows -1
stars = 1

for i in range(rows):
    print(SPASE*spases+STAR*stars+SPASE*spases)
    stars += 2
    spases -= 1

  

  