from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# How to switch to an iframe and submit a date by hard core value#########
frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)
# driver.find_element(By.ID, "datepicker").send_keys("08/30/2022")

# How to select the month and year by automation (By loop statement)
date = "25"
month = "May"
year = "2025"
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
while True:
    month_name = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year_name = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if month_name == month and year_name == year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
# Second Stage -Select date ##############
date_name = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for d in date_name:
    if d.text == date:
        d.click()
        break


