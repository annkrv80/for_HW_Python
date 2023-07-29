import pytest
import json
from Task_03_13 import Project
from Task_02_13 import User, add_user_to_file
from unittest.mock import patch


def test_user_create():
    user = User('505', 'Lina', 5)
    assert user.user_id == '505', 'Incorrect ID'
    assert user.name == 'Lina', 'Incorrect name'
    assert user.level == 5 , 'Incorrect level'


def test_add_user_to_file():
    with patch('builtins.input', return_value='777 Makar 5'):
        add_user_to_file('test_users.json')
    

@pytest.fixture
def test_project():
    return Project.load('users.json')

def test_login(test_project):
    assert test_project.login('100', 'Anna') == test_project.admin, 'User not found' 


def test_add_user(test_project):
    test_project.admin = User('100', 'Anna', 1)
    test_project.add_user('014', 'Boss', 2)

if __name__ == '__main__':
    pytest.main(['-v'])
   

