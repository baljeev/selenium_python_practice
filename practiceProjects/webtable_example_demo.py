# Count number of rows and columns in the table
# Read specific row and columns data
# Read all the row and columns data
# Read data based on condition (List book name whose author is a particular person)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
driver.find_element(By.ID, "accept-choices").click()

# Count number of rows and columns in the table
num_rows = len(driver.find_elements(By.XPATH, "//table[@id='customers']//tr"))
num_columns = len(driver.find_elements(By.XPATH, "//table[@id='customers']//tr/th"))
# print(num_rows)
# print(num_columns)

# Read specific row and columns data
# data = driver.find_element(By.XPATH, "//table[@id='customers']//tr[3]/td[2]").text
# print(data)

# Read all the row and columns data
# for r in range(2,num_rows+1):
#     for c in range(1,num_columns + 1):
#         data = driver.find_element(By.XPATH, "//table[@id='customers']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end="    ")
#     print()

# Read data based on condition (List book name whose author is a particular person)
for r in range(2, num_rows + 1):
    cty_name = driver.find_element(By.XPATH, "//table[@id='customers']//tr[" + str(r) + "]/td[3]").text
    if cty_name == "Canada":
        com_name = driver.find_element(By.XPATH, "//table[@id='customers']//tr[" + str(r) + "]/td[1]").text
        cont_name = driver.find_element(By.XPATH, "//table[@id='customers']//tr["+str(r)+"]/td[2]").text
        print(com_name, " ", cont_name, "  ", cty_name)

driver.close()
