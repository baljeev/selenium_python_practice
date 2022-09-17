import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("https://www.snapdeal.com/")
driver.maximize_window()
driver.find_element(By.ID, "inputValEnter").send_keys("Mobile Phone")
driver.find_element(By.XPATH, "//span[@class='searchTextSpan']").click()