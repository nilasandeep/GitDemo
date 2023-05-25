import pytest
#yield  to run after test aand fixture to run before test
#@pytest.fixture()
#def setup():
    #print("This will be executed first")
    #yield
    #print("This will be executed last")

@pytest.mark.usefixtures("setup")
class TestExample:


     def test_fixtureDemo(self):
         print("This will execute steps in fixturedemo method ")


     def test_fixtureDemo1(self):
        print("This will execute steps in fixturedemo method ")

     def test_fixtureDemo2(self):
        print("This will execute steps in fixturedemo method ")

     def test_fixtureDemo3(self):
            print("This will execute steps in fixturedemo method ")