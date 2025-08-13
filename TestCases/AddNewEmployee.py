import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
import time
from AUTOMATION.pageObjects import NEW_EMP

@pytest.fixture
def driver():
    # chrome_options = Options()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield driver
    driver.quit()

def test_employee_details_flow(driver):
    base_url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    attachment_path = "AUTOMATION/orgTest.jfif"

    # Open the site
    driver.get(base_url)

    # Create page object
    emp_page = NEW_EMP(driver)

    # 1. Login
    emp_page.login(username, password)
    time.sleep(3)

    # 2. Go to "My Info"
    emp_page.address_info()[0].click()
    time.sleep(2)

    # 3. Go to Contact Details tab
    emp_page.emp_contact()
    time.sleep(2)

    # 4. Fill Address Part 1
    emp_page.address_employee("Street 1", "Street 2", "Nairobi")
    time.sleep(1)

    # 5. Fill Address Part 2
    emp_page.address_employee2("Nairobi County", "00100")
    time.sleep(1)

    # 6. Fill Telephone Numbers
    emp_page.telephone_phone("020123456", "0712345678", "0412345678")
    time.sleep(1)

    # 7. Fill Emails
    emp_page.mail("work@example.com", "other@example.com")
    time.sleep(2)

    # 8. Upload Attachment
    emp_page.attachment_uploading(attachment_path)
    time.sleep(2)

    assert "Contact Details" in driver.page_source
