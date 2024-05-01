from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.find_element(By.ID,"datepicker").click()

all_dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")

for dates in all_dates:
    print(dates.text)
    if dates.text=="25":
        dates.click()
        break