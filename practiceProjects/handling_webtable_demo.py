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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Count number of rows and columns in the table
num_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
num_colum = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))
# print(num_rows)
# print(num_colum)

# Read specific row and columns data
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[4]/td[1]")
# print(data.text)  # Learn JS
# data1 = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[6]/td[4]")
# print(data1.text) # 2000

# Read all the row and columns data
# for r in range(2, num_rows + 1):
#     for c in range(1, num_colum + 1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]")
#         print(data.text, end="   ")
#
#     print("")

# Read data based on condition (List book name whose author is a particular person)

for r in range(2,num_rows + 1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if author_name == "Amit":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        print(book_name, "  ", author_name)





driver.close()