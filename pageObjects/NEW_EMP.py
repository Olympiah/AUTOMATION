from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class EmployeeDetails:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.username = (By.CSS_SELECTOR, "input[placeholder='Username']")
        self.password = (By.CSS_SELECTOR, "input[placeholder='Password']")
        self.submit = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        self.my_info = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]")
        self.info = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]")

        self.first_street = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input")
        self.contact = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a")
        self.second_street = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input")
        self.city = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input")
        self.state_province = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input")
        self.zip_postal = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input")
        self.country = (By.CLASS_NAME, "oxd-select-text-input")

        self.home = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input")
        self.mobile = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input")
        self.work = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input")
        self.work_email = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input")
        self.other_email = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input")
        self.btn_save = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button")
        self.btn_attachment = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button")
        self.upload_attachment = (By.CSS_SELECTOR, "input[type='file']")
        self.save_attachment = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[3]/button[2]")

    # Methods
    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submit).click()

    def address_info(self):
        return self.driver.find_elements(*self.my_info)

    def emp_contact(self):
        contact_info = self.wait.until(EC.element_to_be_clickable(self.contact))
        contact_info.click()

    def address_employee(self, s1, s2, city_emp):
        self.driver.find_element(*self.first_street).send_keys(s1)
        self.driver.find_element(*self.second_street).send_keys(s2)
        self.driver.find_element(*self.city).send_keys(city_emp)
        self.driver.execute_script("window.scrollBy(0, 65)")

        nationality_button = self.driver.find_elements(*self.country)[0]
        nationality_button.send_keys("m")
        nationality_button.send_keys(Keys.ARROW_DOWN)
        nationality_button.send_keys(Keys.ARROW_DOWN)
        nationality_button.send_keys(Keys.ENTER)

    def address_employee2(self, state, zipcode):
        self.driver.find_element(*self.state_province).send_keys(state)
        self.driver.find_element(*self.zip_postal).send_keys(zipcode)
        self.driver.execute_script("window.scrollBy(0, 98)")

    def telephone_phone(self, home_emp, mobile_emp, work_number):
        self.driver.find_element(*self.home).send_keys(home_emp)
        self.driver.find_element(*self.mobile).send_keys(mobile_emp)

        work_elem = self.driver.find_element(*self.work)
        work_elem.send_keys(Keys.CONTROL + "a")
        work_elem.send_keys(Keys.DELETE)
        work_elem.send_keys(work_number)

    def mail(self, email_emp, email):
        self.driver.find_element(*self.otheremail).send_keys(email)
        work_email_elem = self.driver.find_element(*self.workemail)
        work_email_elem.send_keys(Keys.CONTROL + "a")
        work_email_elem.send_keys(Keys.DELETE)
        work_email_elem.send_keys(email_emp)
        self.driver.find_element(*self.btn_save).click()

    def attachment_uploading(self, path):
        self.driver.find_element(*self.btn_attachment).click()
        self.driver.find_element(*self.upload_attachment).send_keys(path)
        self.driver.find_element(*self.save_attachment).click()
