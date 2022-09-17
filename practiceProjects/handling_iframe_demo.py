# switch_to.frame(name of the frame)
# switch_to.frame(id of the frame)
# switch_to.frame(web element)
# switch_to.frame[0]

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()
# Switching to the first frame
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()
time.sleep(2)

# switching to the second frame
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "Capabilities").click()
driver.switch_to.default_content()
time.sleep(2)
# switching to the third frame
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "(//ul[@class='subNavList']/li[4]/a)[1]").click()
#