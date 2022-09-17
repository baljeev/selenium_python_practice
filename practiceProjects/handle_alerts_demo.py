from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class demoalerts():
    def demo_alert(self):
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver.implicitly_wait(5)
            driver.get("https://the-internet.herokuapp.com/javascript_alerts")
            driver.maximize_window()
            driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
            alert_window = driver.switch_to.alert
            print(alert_window.text)
            alert_window.accept()  # This will click ok on the alert window
alerts =demoalerts()
alerts.demo_alert()
# alert_window.dismiss()  # This will click cancel on the alert window
# act_result = "You entered: Welcome"
# exp_result = driver.find_element(By.XPATH, "//p[@id='result']").text
# print(exp_result)
# if exp_result == act_result:
#     print("Test is passed")
# else:
#     print("test is failed")

