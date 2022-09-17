import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.keralartc.com/main.html")
driver.maximize_window()
time.sleep(2)
more_link = driver.find_element(By.XPATH, "//a[@id='dropdownMenuButton']")
network_link = driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Network']")
action = ActionChains(driver)
action.move_to_element(more_link).click().perform()
time.sleep(2)
action.move_to_element(network_link).click().perform()
time.sleep(2)
if driver.title == "KeralaRTC Official Website - keralartc.com":
    print(" test passed")
else:
    print("test failed")
driver.close()