class MyException(Exception):
    pass


class GradeException(MyException):
    def __init__(self, grade):
        self.grade = grade
    
    def __str__(self):
        return f'{self.grade} должна быть в диапазоне от 2 до 5'


class TestException(MyException):
    def __init__(self, result):
        self.result = result
    

    def __str__(self):
        return f'{self.result} должн быть в диапазоне от 0 до 100'