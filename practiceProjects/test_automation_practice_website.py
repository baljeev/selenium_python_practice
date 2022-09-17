from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# current_title = driver.title
# print(current_title)
# print(driver.current_url)
# driver.find_element(By.ID, "name").send_keys("John")
# driver.find_element(By.ID, "phone").send_keys("0123456")
# driver.find_element(By.ID, "email").send_keys("123@gmail.com")
# driver.find_element(By.ID, "password").send_keys("abcdef")
# driver.find_element(By.ID, "address").send_keys("This is my Python programming")
# driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
#
# female = driver.find_element(By.ID, "female")
# male = driver.find_element(By.ID, "male")
# if female.is_selected():
#     female.click()
#
# else:
#     male.click()
# selecting all the week name  ###########################################
days_week = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains (@id,'day')]")
# for day in days_week:
#     day.click()


# Clicking only the selected week name ##########################################
# for d in days_week:
#     week_name = d.get_attribute("id")
#     if week_name == "monday" or week_name == "thursday":
#         d.click()

# Clicking only 3 days from the bottom #############################
for i in range(len(days_week)-3 , len(days_week)):
    days_week[i].click()


# clicking  only 3 days from first ################################
# for i in range(len(days_week)):
#     if i < 3:
#         days_week[i].click()

# drop_box = driver.find_element(By.XPATH, "//select[@class='custom-select']")
# drop_ele = Select(drop_box)
# # drop_ele.select_by_visible_text("Turkey")
# # drop_ele.select_by_index(1)
# drop_ele.select_by_value("3")
#
# tools = driver.find_elements(By.XPATH, "//div[@class='custom-control custom-checkbox']")
# # print(len(tools))
# for course in tools:
#     course.click()
