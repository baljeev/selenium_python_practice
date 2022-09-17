import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("https://www.amazon.co.uk/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Samsung Phones")
driver.find_element(By.XPATH, "//div[@class='nav-search-submit nav-sprite']").click()

driver.find_element(By.XPATH, "//span[@id='a-autoid-0']").click()
driver.find_element(By.XPATH, "//*[@id='p_76/419159031']/span/a/div[1]/label").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@id='p_89/Samsung']//label").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='£100 to £200']").click()

for i in range(6):
    phone_names = driver.find_elements(By.XPATH,
                                       "//span[contains(@class,'a-size-base-plus a-color-base a-text-normal')]")
    phone_values = driver.find_elements(By.XPATH, "//span[contains(@class,'a-price-whole')]")
    my_phone = []
    my_rate = []
    for names in phone_names:
        print(names.text)
        my_phone.append(names.text)
    for values in phone_values:
        # print(values.text)
        my_rate.append(values.text)
    finalList = zip(my_phone, my_rate)
    for data in list(finalList):
        print(data)
        time.sleep(5)
    driver.find_element(By.XPATH,
                        "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']").click()
driver.close()
