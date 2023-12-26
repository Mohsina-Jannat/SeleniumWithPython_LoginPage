import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(300)
driver.get("https://www.sailor.clothing/login")
driver.maximize_window()

email = driver.find_element(By.NAME, "email")
email.send_keys("mohsinasust@gmail.com")

passwrd = driver.find_element(By.NAME, "password")
passwrd.send_keys("Sailor@1234")

loginBtn = driver.find_element(By.XPATH, "/html/body/div/main/section/div/div/div/div/div/div[1]/form/button")
loginBtn.click()

#Sucessful login indicates navigation to profile page after login and by verifying profile page header

time.sleep(5)

getUrl = driver.current_url

expectedUrl = "https://www.sailor.clothing/profile"

assert getUrl == expectedUrl

header = driver.find_element(By.XPATH, "/html/body/div/main/section[2]/div/div/div[2]/div/div/fieldset/legend").text

if header == "PERSONAL INFORMATION":
    print("User login is verified successfully")

time.sleep(2)

driver.quit()