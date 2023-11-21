class MyException(Exception):
    pass

class ValueException(MyException):
    def __init__(self, length, width ):
        self.length = length
        self.width = width

    def __str__(self):
        return f'{self.length} и {self.width} должны быть больше 0'