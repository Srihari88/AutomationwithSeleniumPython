from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5000)

parent_window=driver.current_window_handle

driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()

child_windows=driver.window_handles


for child in child_windows:
    if parent_window!=child:
        driver._switch_to.window(child)
        print("Title is:", driver.title)
        driver.find_element(By.CSS_SELECTOR,'[name="EmailHomePage"]').send_keys("srihari@gmail.com")
        driver.implicitly_wait(3000)
        driver.close()
driver.switch_to.window(parent_window)
print(driver.title)
