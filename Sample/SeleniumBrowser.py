import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")

#Get the window title
print(driver.title)

driver.find_element(By.XPATH, "(//a[@href='https://courses.rahulshettyacademy.com/sign_up'])[1]").click()
driver.find_element(By.XPATH,"(//button[@name='sign_up_method'])[1]").click()
time.sleep(10)
driver.find_element(By.ID,"user_name").send_keys("rajini")
driver.find_element(By.ID,"user_email").send_keys("rajini5@gmail.com")
driver.find_element(By.ID,"password").send_keys("Test@123")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(10)
value = driver.find_element(By.XPATH,"//div[text()='Please confirm your email to fully activate your account. You can do this by clicking the link in the email confirmation we sent you.']").text
print(value)
assert "Please confirm your email to fully activate your account." in value

driver.find_element(By.XPATH,"(//button[@type='button'])[3]").click()
dropdown = driver.find_elements(By.XPATH,"//ul[@id='courses-dropdown']/li/a")

for items in dropdown:
    print(items.text)
    if items.text == "AdminUser":
        items.click()
time.sleep(10)

driver.close()