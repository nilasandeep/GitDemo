# class to show data load  from fixture
# in what scenario you are forced to give fixture name as parameter in the test method, though it is already declared at class level- in case of fixtures that return data
# datadriven and parametrization can be done with return statemants in tuple format
# when you define fixture scope to class only, , it will run once before class is initiated and at end after all class methods are executed


import pytest

from pytestDemo.BaseClass import BaseClass
@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editprofile(self, dataLoad):  # passing dataLoad in parameter since this fixture is returning data
        self.getLogger()
        print(dataLoad)  # will print as a tuple
        print(dataLoad[0])  # if you want  to print in separate rows
        print(dataLoad[1])
