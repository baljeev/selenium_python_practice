import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.snapdeal.com/")
driver.maximize_window()
driver.find_element(By.ID, "inputValEnter").send_keys("Mobile Phone")
time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='searchTextSpan']").click()
time.sleep(2)
slider_left = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
slider_right = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")
action = ActionChains(driver)

### left slider #############################

# action.click_and_hold(slider_left).pause(1).move_by_offset(50,0).release().perform() ##### click and hold method
# action.drag_and_drop_by_offset(slider_left,60,0).perform() ########## drag and drop method
action.move_to_element(slider_left).pause(1).click_and_hold(slider_left).move_by_offset(70,0).release().perform()
time.sleep(3)

## Right Slider #############
action.click_and_hold(slider_right).pause(1).move_by_offset(-50,0).release().perform()