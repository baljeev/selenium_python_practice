import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Selenium")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
search_links = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']/a")
for link in search_links:
    link.click()
    print(link.text)
window_handles = driver.window_handles
print(window_handles)
for windid in window_handles:
    driver.switch_to.window(windid)
    print(driver.title)
    if driver.title == "Selenium disulfide - Wikipedia" or driver.title == "Selenium (software) - Wikipedia":
        driver.close()
driver.quit()
# print(window_handles)
# frstwind_id = window_handles[1]  #
# secwind_id = window_handles[2]
# thiwind_id = window_handles[3]
# fourwind_id = window_handles[4]
# fifwind_id = window_handles[5]
#
# driver.switch_to.window(frstwind_id)
# print("This is first window;", driver.title)  # Selenium - Wikipedia
# driver.switch_to.window(secwind_id)
# print("This is second window;", driver.title)  # Selenium in biology - Wikipedia
# driver.switch_to.window(thiwind_id)
# print("This is third window;", driver.title)  # Selenium (software) - Wikipedia
# driver.switch_to.window(fourwind_id)
# print("This is fourth window;", driver.title)  # Selenium disulfide - Wikipedia
# driver.switch_to.window(fifwind_id)
# print("This is fifth window;", driver.title)  # Selenium dioxide - Wikipedia
