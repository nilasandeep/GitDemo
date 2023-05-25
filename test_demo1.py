# any pytest file should start with 'test_' or end with '_test'
# as per pytest standards, what ever code we write, we have to write the code in functions
# pytest method names should start with test
import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("hello")

def test_crossBrowser(crossBrowser): #we have to pass the fixture name "crossBrowser" as parameter in test method
    print(crossBrowser) #first time wuill print chrome, second time, firefox etc
    #you can give like print(crossBrowser[1]) to print the 1st position of each item in tuple

