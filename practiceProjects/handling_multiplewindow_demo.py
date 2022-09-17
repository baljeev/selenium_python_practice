import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(3)
win_handles = driver.window_handles
par_win = win_handles[0]
child_win = win_handles[1]
# print("parent window id is:", par_win)
# print("Child window id is :", child_win)
driver.switch_to.window(par_win)
print(driver.title)
driver.switch_to.window(child_win)
print(driver.title)
