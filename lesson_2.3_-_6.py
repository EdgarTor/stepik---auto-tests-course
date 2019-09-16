from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(link)

    journey_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = submit]')
    journey_btn.click()

    main_window = driver.window_handles[0]
    second_window = driver.window_handles[1]

    driver.switch_to.window(second_window)

    x = driver.find_element(By.ID, 'input_value')
    x_value = int(x.text)

    result = str(calc(x_value))

    answer_input = driver.find_element(By.ID, 'answer')
    answer_input.send_keys(result)

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    submit_btn.click()
finally:
    time.sleep(10)
    driver.quit()