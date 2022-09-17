from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.ID, "product_549").click()
driver.find_element(By.ID, "travname").send_keys("John")
driver.find_element(By.ID, "travlastname").send_keys("Smith")
driver.find_element(By.ID, "order_comments").send_keys("This is a Dummy Ticket")

date = "25"

driver.find_element(By.XPATH, "//input[@id='dob']").click()
month_drop = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month_drop.select_by_visible_text("Apr")
year_drop = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
year_drop.select_by_visible_text("2021")

# Approach 1 for selecting the date #######################
# dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//tr/td/a")
# for d in dates:
#     if d.text == date:
#         d.click()
#         break

# Approach - 2 for selecting the date
driver.find_element(By.XPATH, "//a[normalize-space()='25']").click()
driver.find_element(By.XPATH, "//*[@id='sex_1']").click()
