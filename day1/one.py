from selenium import webdriver
from selenium.webdriver.common.by import By

user_name="[name='username']"
pass_word="[name='password']"
login="[type='submit']"
dropdown="[class='oxd-userdropdown-name']"
logout="//a[contains(text(),'Logout')]"


driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5000)
driver.find_element(By.CSS_SELECTOR,user_name).send_keys("Admin")
my_Username=driver.find_element(By.CSS_SELECTOR,user_name).get_attribute("value")

# Assert the input value

assert  my_Username in "Admin"
print(my_Username)
driver.implicitly_wait(3000)
driver.find_element(By.CSS_SELECTOR,pass_word).send_keys("admin123")
driver.implicitly_wait(3000)
submit_button_text=driver.find_element(By.CSS_SELECTOR,login).text
print(submit_button_text)
driver.find_element(By.CSS_SELECTOR,login).click()
driver.implicitly_wait(7000)
print("Browser opened")



# Verify the title of the page

page_title=driver.title
print(page_title)

# get page URL

current_Page_url=driver.current_url
print(current_Page_url)

# get cookies

driver.implicitly_wait(10)
