import csv
from pathlib import Path
from Exept_02 import GradeException, TestException

class Text:
    def __set_name__(self, owner, name):
        self.name_param = ' ' + name
   
    def __get__(self, instance, owner):
        return getattr(instance, self.name_param)
    
    def __set__(self, instance, value):
        self.valedate(value)
        setattr(instance, self.name_param, value)

    def valedate(self, value):
        if not str(value).isalpha():
            raise ValueError ('ФИО должно состоять только из букв')
        if not str(value).istitle():
            raise ValueError ('ФИО должно начитаться с заглавной буквы')


class Student:
    surname = Text()
    name =  Text()
    patronymic = Text()
    _subjects = None
    

    def __init__(self, surname, name, patronymic, subjects: Path):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.subjects = subjects
    
    @property
    def subjects(self):
        return self._subjects
    
    @subjects.setter
    def subjects(self, sub: Path):
        self._subjects = {}
        try:
            with open(sub, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for subject in reader:
                    self.subjects[subject[0]] = {'grades': [], 'test_results': []}
        except FileNotFoundError:
            print (f'файл {sub}  не найден')
          
                    
    def add_grade(self, subject, grade):
        if grade < 2 or grade > 5:
            raise GradeException(grade)
        self.subjects[subject]['grades'].append(grade)
     

    def add_redult_test(self, subject, result):    
        if result < 0 or result > 100:
            raise TestException(result)
        self.subjects[subject]['test_results'].append(result)  

    def average_resuit_test(self, subject):
        test_results = self.subjects[subject]['test_results']
        if len(test_results) == 0:
            return 0
        return sum(test_results) / len(test_results)
    
    def overall_average_grade(self):
        grades = []
        for subject in self.subjects.values():
            grades.extend(subject['grades'])
        if len(grades) == 0:
            return 0
        return sum(grades) / len(grades)


    def __str__(self):
        result =  f'{self.surname} {self.name} {self.patronymic}. Средний балл по всем предметам = \
{self.overall_average_grade()}\n'
        for key, value in self.subjects.items():
           result +=  f'Средний бал по тестам {key} = {std_1.average_resuit_test(key)}\n'
        return result

if __name__ == '__main__':
    std_1 = Student('Ivanova','Anna', 'Yurevna', Path ('sub.csv'))
    std_1.add_grade('Математика', 5)
    std_1.add_redult_test('Математика', 98)
    std_1.add_grade('Физика', 4)
    std_1.add_grade('Математика', 0)
    std_1.add_redult_test('Русский язык', 100)
    std_1.add_grade('Русский язык', 3)
    std_1.add_redult_test('Физика', 3)
    std_1.add_redult_test('Математика', 66)
    std_1.add_redult_test('Физика', 35)
    std_1.add_grade('Математика', 4)
    std_1.add_grade('Физика', 3)
    std_1.add_grade('Русский язык', 5)
    print(std_1)