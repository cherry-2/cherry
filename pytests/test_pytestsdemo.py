import pytest


@pytest.mark.usefixtures("setup")
class TestExamples:
    def test_firstprogram(self):
        print("hello")

    def test_firstprogram1(self):
        print("good morning")

    def test_firstprogram2(self):
        print("doing good")

    @pytest.mark.smoke
# @pytest.mark.skip
    def test_secondprogram(self):
        greet = "hi"
        assert greet == "hi"