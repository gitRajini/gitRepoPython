import pytest


def test_additional():
    a= 10
    b= 20

    assert a==10, 'Not equal'
@pytest.mark.smoke
def test_substraction():
    c=10
    d=5
    print("Substraction of 2 number: ",  c-d)
@pytest.mark.smoke
def test_multiplication():
    e=5
    f=5
    assert e*f == 25, "Not matching"
