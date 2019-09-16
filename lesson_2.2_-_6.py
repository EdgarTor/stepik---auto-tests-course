from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://SunInJuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    x = driver.find_element(By.ID, 'input_value')
    x_value = int(x.text)

    result = calc(x_value)

    input_answer = driver.find_element(By.ID, 'answer')
    input_answer.send_keys(result)

    captcha = driver.find_element(By.ID, 'robotCheckbox')
    captcha.click()

    robot_rule = driver.find_element(By.ID, 'robotsRule')
    driver.execute_script(
        'return arguments[0].scrollIntoView(true);', robot_rule
    )
    robot_rule.click()

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    submit_btn.click()
finally:
    time.sleep(10)
    driver.quit()