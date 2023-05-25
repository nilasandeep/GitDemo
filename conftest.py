#To pass data from

import pytest


@pytest.fixture(scope="class")
def setup():
    print("This will be executed first")
    yield
    print("This will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return["Nila", "Rajendran", "nilarajendran1312@gmail.com"] #returning tuples
#parametrization

#@pytest.fixture(params=["chrome", "Firefox", "IE"])
#def crossBrowser(request):
    #return request.param #code for this is in the file test_demo1

#to pass multiple data in first run

@pytest.fixture(params=[("chrome", "Nila", "Rajendran"), ("Firefox", "Nandika", "Anand"),("IE", "Sandeep","Anand")])
def crossBrowser(request):
    return request.param
#for above program in first run will consider chrome, Nila and Rajendran and second run - firefoxx, nandika and anand