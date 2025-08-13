import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as Exp
# for identifying element in page
from selenium.webdriver.common.by import By

serviceC = Service(excexutable_path='C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

# creating driver object for chrome - will manage lifecycle of this particular instance
driver = webdriver.Chrome(service=serviceC)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(3) # to allow page to load

# access the login details by respective elements
# username = driver.find_element(By.NAME, value="username")
username = wait(driver, timeout=10).until(Exp.presence_of_element_located((By.NAME, "username")))
password = driver.find_element(By.NAME, value="password")

# //button[@type='submit']
login_btn = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

# action
username.send_keys("Admin")
password.send_keys("admin123")
login_btn.click()
time.sleep(3)
# After successfully logging in, confirm the right "Title" is displayed
actual_Title = driver.title
expected_Title = 'OrangeHRM'

if expected_Title != actual_Title:
    raise AssertionError('Automation Testing Failed')
else:
    print("Login and Title Verification successful")

driver.close()