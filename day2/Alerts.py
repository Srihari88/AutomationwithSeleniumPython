from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.implicitly_wait(3000)
driver.find_element(By.XPATH,"//input[@title='Sign in']").click()

alt=driver.switch_to.alert
alt_text=alt.text
driver.implicitly_wait(3000)
print(alt_text)
alt.accept()

