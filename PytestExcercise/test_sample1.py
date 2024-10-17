import pytest

@pytest.mark.xfail
def test_text1():
    print("text1...!!!")

@pytest.mark.skip
def test_text2():
    print("text2...!!!")
    a =99
    assert a == 88, 'Not equal'


