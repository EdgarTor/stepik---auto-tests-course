from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects2.html'

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    num1 = driver.find_element(By.ID, 'num1')
    num1_value = int(num1.text)

    num2 = driver.find_element(By.ID, 'num2')
    num2_value = int(num2.text)

    result = num1_value + num2_value

    select = Select(driver.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result))

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    submit_btn.click()
finally:
    time.sleep(10)
    driver.quit()