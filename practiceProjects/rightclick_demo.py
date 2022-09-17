import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
rightcllick_button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
edit_button = driver.find_element(By.XPATH, "//span[normalize-space()='Edit']")
time.sleep(2)
main_frame = driver.find_element(By.XPATH, "//iframe[@id='gdpr-consent-notice']")
driver.switch_to.frame(main_frame)
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='save']/span[1]/div/span").click()
actions = ActionChains(driver)
actions.context_click(rightcllick_button).perform()
time.sleep(2)
edit_button.click()
time.sleep(2)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
time.sleep(3)