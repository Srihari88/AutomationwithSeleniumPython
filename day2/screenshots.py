from selenium import webdriver
import os

driver=webdriver.Chrome()

driver.get("https://www.google.com")
driver.get_screenshot_as_file(os.getcwd()+"/screenshots/"+"google.png")
driver.quit()