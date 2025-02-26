import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    username = "sim@abv.bg"
    password = "sim123"
    return [username, password]


# @pytest.fixture(scope="module")
# def driver():
#      _driver = webdriver.Edge()
#      yield _driver
#      _driver.quit()

@pytest.fixture(params=["Edge","firefox"],scope='module')
def driver(request):
    if request.param=="Edge":
        _driver=webdriver.Edge()
    if request.param=="firefox":
        _driver=webdriver.Firefox()
    yield _driver
    _driver.quit()