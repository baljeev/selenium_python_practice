import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class skyscanner():
    def demo_skyscanner(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.akbartravels.com/in/flight")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.XPATH, "//label[@for='mat-radio-3-input']//div[@class='mat-radio-label-content']").click()
        time.sleep(3)
        from_dest =  driver.find_element(By.XPATH, "//li[@id='liFrom']")
        time.sleep(2)
        from_dest.click()
        from_dest.send_keys("New Delhi")
        from_dest.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@class='searchinput']").send_keys("New Delhi")

        # from_dest.send_keys("Cochin")
        # from_dest.send_keys(Keys.ENTER)
        time.sleep(5)

            # dest_list = driver.find_elements(By.XPATH, "//div[@class='search-list']/ul/li")


        #
        # time.sleep(2)
        # btn_rtn.click()






demosales =skyscanner()
demosales.demo_skyscanner()