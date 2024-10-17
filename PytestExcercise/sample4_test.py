import pytest


@pytest.mark.usefixtures("Data")
class TestData:

    def test_Calculate(self,Data):
        username = Data[0]
        password = Data[1]

        print(username, password)
        print("Done")


