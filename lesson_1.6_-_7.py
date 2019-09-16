from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    input_elements = driver.find_elements(By.TAG_NAME, 'input')
    for input_element in input_elements:
        input_element.send_keys('text')

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_btn.click()
finally:
    time.sleep(30)
    driver.quit()
