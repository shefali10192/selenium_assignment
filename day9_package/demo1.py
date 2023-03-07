import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from datetime import date


driver= webdriver.Chrome()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20)
driver.get("http://demo.openemr.io/b/openemr/")
driver.find_element(By.ID, "authUser").send_keys("admin")
driver.find_element(By.ID, "clearPass").send_keys("pass")
# Using XPath Directly#
driver.find_element(By.XPATH, "//option[contains(@value,'18')]").click()
select_lang = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
select_lang.select_by_visible_text("English (Indian)")
driver.find_element(By.ID, "login-button").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//div[text()='Patient']").click()
driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))
time.sleep(5)
driver.find_element(By.ID, "form_fname").send_keys("Shefali")
driver.find_element(By.ID, "form_lname").send_keys("Shah")
today = date.today()
d4 = today.strftime("%Y-%m-%d")

driver.find_element(By.ID, "form_DOB").send_keys(d4)
driver.find_element(By.XPATH, "//option[text()='Female']").click()
driver.find_element(By.ID, "create").click()

driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()

driver.switch_to.default_content()

wait=WebDriverWait(driver,50)
wait.until(expected_conditions.alert_is_present())

actual_alert=driver.switch_to.alert.text
print(actual_alert)

driver.switch_to.alert.accept()

time.sleep(5)
driver.quit()