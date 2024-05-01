from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5000)
driver.find_element(By.CSS_SELECTOR,"[data-testid='open-registration-form-button']").click()
time.sleep(3)


# Handling dropdown using date
day=driver.find_element(By.CSS_SELECTOR,"[id='day']")
dayDD=Select(day)
dayDD.select_by_value('5')
time.sleep(3)

# Handling dropdowns
month=driver.find_element(By.CSS_SELECTOR,"[id='month']")
monDD=Select(month)
monDD.select_by_index('5')
time.sleep(3)


# Handling dropdowns
year=driver.find_element(By.CSS_SELECTOR,"[id='year']")
yearDD=Select(year)
yearDD.select_by_visible_text('2020')
time.sleep(3)


# List down the toal values present in the dropdown

total_months=monDD.options
print(total_months)
print(len(total_months))

for month_names in total_months:
    print(month_names.text)


