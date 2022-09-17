# capture window id
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# get single window id ######################################
window_id = driver.current_window_handle
print(window_id)

# get multiple window id's  ######################################
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
window_ids = driver.window_handles
# parent_window = window_ids[0]
# child_window = window_ids[1]
# driver.switch_to.window(child_window)
# print("Child window id is:", driver.title)
# driver.switch_to.window(parent_window)
# print("Parent window id is:", driver.title)


# Approach -2
# close selected window through automation
for win_id in window_ids:
    driver.switch_to.window(win_id)
    if driver.title == "OrangeHRM":
        driver.close()


# for wind_id in window_ids:
#     driver.switch_to.window(wind_id)
#     time.sleep(3)
#     if driver.title == "OrangeHRM":
#         driver.close()



