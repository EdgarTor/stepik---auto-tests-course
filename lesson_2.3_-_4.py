from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    journey_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    journey_btn.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    x = driver.find_element(By.ID, 'input_value')
    x_value = int(x.text)

    result = calc(x_value)

    answer_input = driver.find_element(By.ID, 'answer')
    answer_input.send_keys(str(result))

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    submit_btn.click()
finally:
    time.sleep(10)
    driver.quit()