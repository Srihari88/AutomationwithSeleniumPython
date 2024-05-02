from openpyxl.workbook import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By

titiles_name=[]
prices_values=[]

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10000)

driver.find_element(By.CSS_SELECTOR,"[id='twotabsearchtextbox']").send_keys("Samsung")
driver.find_element(By.CSS_SELECTOR,"[id='nav-search-submit-button']").click()

sumsang_names=driver.find_elements(By.CSS_SELECTOR,"[class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")

price_ranges=driver.find_elements(By.CSS_SELECTOR,"[data-a-size='xl']")

for names in sumsang_names:
    titiles_name.append(names.text)

print("*"*50)

for price_value in price_ranges:
    prices_values.append(price_value.text)


final_values=zip(titiles_name,prices_values)


for data in list(final_values):
    print(data)

print("Part-1")

wb=Workbook()
wb['Sheet'].title="Sumsang Data"
sh1=wb.active

sh1.append(['Name','Price'])


for x in list(final_values):
    sh1.append(x)

wb.save("srihari.xlsx")

print("Part-2")




