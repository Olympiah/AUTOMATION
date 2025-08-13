# for identifying element in page
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):  # passing driver from text case
        # locators
        self.driver = driver
        self.username_field = (By.NAME, 'username')
        self.password_field = (By.NAME, 'password')
        self.login_btn = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        self.invalid_cred = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/p')

    # methods
    # def enter_username(self, username):
    #     # unpacking the tuple
    #     self.driver.find_element(*self.username_field).send_keys(username)
    def login(self, username, password):
        # unpacking the tuple
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
