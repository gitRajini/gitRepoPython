import pytest

@pytest.mark.usefixtures("setup")
class Testing:
    def test_condition(self):  # Execute second
        msg = "Hari Om"
        assert msg == "Hari Om", "message not matching"
        print("Executed Second")

    def test_condition1a(self):  # Execute second
        msg = "Hari Om"
        assert msg == "Hari Om", "message not matching"
        print("Executed Third")

    def test_condition2a(self):  # Execute second
        msg = "Hari Om"
        assert msg == "Hari Om", "message not matching"
        print("Executed Fourth")
