import pytest
from selenium import webdriver

from AUTOMATION.pageObjects.LOGIN_PAGE import LoginPage


@pytest.fixture(scope='function')
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)
    yield driver  # gives driver back to fn and once executed setup in control
    driver.close()


def test_login(setup):
    #  accessing curr state of driver
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username="Admin",password="admin123")

    assert 'OrangeHRM' in driver.title, "Test Verification Failed"

def test_invalid_login(setup):
    #  accessing curr state of driver
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username="Admin",password="admin1234")

    assert 'OrangeHRM' in driver.title, "Test Failed"
