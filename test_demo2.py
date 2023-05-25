#method name shud have sense
#-k stands for method name execution (specific keywords), -s logs in out put, -v stands for more info metadata
#to run specific test use py.test <filename>
#to run smoke cases , like tagging in cucumber @pytest.mark.smoke to that test case and to run @pytest -m tagname -v -s
# to run all cases but skip one @pytest.mark.skip and then run all cases using py.test -v -s
#if you want to run some test since it has some prerequisite for another testcase, but want to actually skip it from reporting @pytest.mark.xfail
#fixture  is like background in cucumber - @pytest.fixture() and then write the method for fixture, also pass the name of this fixture method as parameter inside the test case method
#conftest file to generelise fixture and make it available to all test caseso
import pytest

#@pytest.mark.smoke
#@pytest.mark.skip
@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi","test failed since condition dint match"

#@pytest.fixture()
#def setup():
    #print("This will be executed first")


def test_fixtureDemo(setup):
    print("This will execute steps in fixturedemo method ")


