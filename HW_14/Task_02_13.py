import json

class User:
    def __init__(self, user_id, name, level):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'Пользователь:\n Индентификационный номер: {self.user_id} \n Имя: {self.name} \n \
Уровень доспупа: {self.level}\n'
    
    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name
    
def add_user_to_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
    except Exception:
        my_dict = {str(level) : {} for level in range(1,8)}
    while True:
        name, user_id, level = input('Введите имя, ID и уровень через пробел: ').split()
        try:
            if user_id not in my_dict[level].keys():
                my_dict[level].update({user_id: name})
                break
            else:
                print('ID должен быть уникальным!!!')
        except KeyError as e:
            print(f'Ошибка ввода уровня {e}')
    print(f'{my_dict = }')

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, indent=1, ensure_ascii=False)
    
if __name__ == '__main__':
    u_2 = User('006', 'Sub', 6)
    u_3 = User('007', 'Andry', 3)
    #print(u_1 == u_2)
    #print(u_1 == u_3)
    filename = 'users.json'
    add_user_to_file(filename)
   