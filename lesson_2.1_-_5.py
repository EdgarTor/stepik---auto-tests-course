from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/math.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    x = driver.find_element(By.ID, 'input_value')
    x_value = x.text

    result = calc(x_value)

    input_answer = driver.find_element(By.ID, 'answer')
    input_answer.send_keys(result)

    captcha = driver.find_element(By.CSS_SELECTOR, 'label[for = "robotCheckbox"]')
    captcha.click()

    robots_rule = driver.find_element(By.CSS_SELECTOR, 'label[for = robotsRule]')
    robots_rule.click()

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    submit_btn.click()
finally:
    time.sleep(10)
    driver.quit()
