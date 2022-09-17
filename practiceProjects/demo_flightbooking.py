import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class flightbooking():
    def demo_flightbooking(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.civictravel.co.uk/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='chkDirect']").click()
        driver.find_element(By.XPATH, "//input[@id='chkFlexibleDate1']").click()
        from_dest =  driver.find_element(By.XPATH, "//input[@id='txtOrigin']")
        from_dest.click()
        from_dest.send_keys("New Delhi")
        from_dest.send_keys(Keys.ENTER)
        alerts =driver.switch_to.alert
        alerts.accept()
        to_dest = driver.find_element(By.XPATH, "//input[@id='txtDestination']")
        to_dest.click()
        to_dest.send_keys("cochin")
        to_dest.send_keys(Keys.ENTER)
        alerts.accept()
        driver.find_element(By.XPATH, "//input[@id='txtDepartDate']").click()
        dep_month =  Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
        dep_month.select_by_visible_text("Nov")
        time.sleep(2)
        dep_year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
        dep_year.select_by_visible_text("2022")
        dep_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td/a")
        for day in dep_dates:
            if day.text == "15":
                day.click()
                break
        driver.find_element(By.XPATH, "//input[@id='txtReturnDate']").click()
        ret_month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
        ret_month.select_by_visible_text("Dec")
        time.sleep(4)
        ret_year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
        ret_year.select_by_visible_text("2022")
        time.sleep(2)
        rtn_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td/a")
        for date in rtn_dates:
            if date.text == "20":
                date.click()
                break
        time.sleep(3)
        list_airline = Select(driver.find_element(By.XPATH, "//select[@id='ddlAirlines']"))
        list_airline.select_by_visible_text("Air India")
        time.sleep(3)
        list_class = Select(driver.find_element(By.XPATH, "//select[@id='ddlClass']"))
        list_class.select_by_value("Business")
        time.sleep(3)
        adults = Select(driver.find_element(By.XPATH, "//select[@id='ddlAdult']"))
        adults.select_by_value("4")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='btnSearch']").click()
        time.sleep(5)
        error_text = driver.find_element(By.XPATH, "//body")
        print(error_text.text)


        #select_month.select_by_visible_text("Nov")
        #time.sleep(3)


demofligh = flightbooking()
demofligh.demo_flightbooking()
