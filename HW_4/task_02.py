#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
#где ключ — значение переданного аргумента,
#а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.


def dict_of_parameters(**kwargs):
    dict_param = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            dict_param.setdefault(value, []).append(key)
        except:
            dict_param.setdefault(str(value), []).append(key)
    return dict_param


print(dict_of_parameters(a=5, str="Hello", c=7, my_list=[1, 2, 3], b=5,
                         my_set={1, 2, 4, 6}, my_f_set=frozenset((1, 4, 7, 2))))
