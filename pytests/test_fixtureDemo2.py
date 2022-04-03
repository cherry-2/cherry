import pytest


@pytest.mark.usefixtures("dataLoad","setup","crossbrowsers")
class TestExample:

    '''def test_editProfile(self, dataLoad):
        print(dataLoad[1])
        print(dataLoad[3])'''
    def test_crossbrowsers(self,request,crossbrowsers):
        print(request.param)

