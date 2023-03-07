import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from datetime import date


driver= webdriver.Chrome()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(30)
driver.get("https://www.royalcaribbean.com/account/create")

if(len(driver.find_elements(By.XPATH, "//div[@class='notification-banner__close']"))) > 0:
    driver.find_element(By.XPATH, "//div[@class='notification-banner__close']").click()

#driver.find_element(By.CSS_SELECTOR,"div[class='header__buttonIcon header__buttonIcon__watchlist']").click()
time.sleep(15)
# driver.find_element(By.XPATH,"//span[text()='Sign In']").click()
#
#
# driver.find_element(By.XPATH,'//a[@href="/account/register"]').click()

#print(driver.window_handles)
#driver.execute_script("document.querySelector(\"input[name='demo59713']\").value = 'Chennai'")

#document.querySelector("a[class='login__create-account login__create-account--royal']")
#driver.execute_script("document.querySelector(\"a[class='login__create-account login__create-account--royal']\").click")



#driver.find_element(By.XPATH, "//a[text()='Create an account']").click()

driver.find_element(By.XPATH, "//input[@data-placeholder='First name/Given name']").send_keys("Dennis")

driver.find_element(By.XPATH, "//input[@data-placeholder='Last name/Surname']").send_keys("Rich")
driver.find_element(By.XPATH,"//span[text()='Month'][1]").click()
driver.find_element(By.XPATH,"//span[normalize-space()= 'April']").click()
driver.find_element(By.ID,"mat-input-3").send_keys("1990")
driver.find_element(By.XPATH, "//span[text()='Day']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='5']").click()


driver.find_element(By.XPATH, "//span[normalize-space()='Country/Region of residence']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='India']").click()

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("abc123")

driver.find_element(By.XPATH, "//span[text()='Select one security question']").click()
driver.find_element(By.XPATH, "//span[contains(text(), 'make or model?')] ").click()
driver.find_element(By.ID, "mat-input-5").send_keys("Model")
driver.find_element(By.ID, "mat-checkbox-2-input").click()
driver.find_element(By.ID, "mat-checkbox-1-input").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Done']").click()
time.sleep(30)