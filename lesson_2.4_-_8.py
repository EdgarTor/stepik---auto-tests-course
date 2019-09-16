from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    home_price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

    book_btn = driver.find_element(By.ID, 'book')
    book_btn.click()

    x = driver.find_element(By.ID, 'input_value')
    x_value = int(x.text)

    result = str(calc(x_value))

    answer_input = driver.find_element(By.ID, 'answer')
    answer_input.send_keys(result)

    submit_btn = driver.find_element(By.ID, 'solve')
    submit_btn.click()
finally:
    time.sleep(10)
    driver.quit()