from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
driver.maximize_window()
driver.find_element(By.ID,'tags').send_keys('S')
driver.implicitly_wait(5000)
listElements=driver.find_elements(By.CSS_SELECTOR,"[class='ui-menu-item'] div")

for dropdown_names in listElements:
    driver.implicitly_wait(5000)
    print("Suggestions found here: ",dropdown_names.text)
    if dropdown_names.text=="Selenium":
        driver.implicitly_wait(5000)
        dropdown_names.click()
        break


