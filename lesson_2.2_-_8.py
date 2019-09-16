from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    first_name = driver.find_element(By.NAME, 'firstname')
    first_name.send_keys('Edgar')

    last_name = driver.find_element(By.NAME, 'lastname')
    last_name.send_keys('Torosyan')

    email = driver.find_element(By.NAME, 'email')
    email.send_keys('example@mail.com')

    files_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files')
    file_path = os.path.join(files_dir, 'test.txt')

    browse = driver.find_element(By.CSS_SELECTOR, 'input[type = "file"]')
    browse.send_keys(file_path)

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    submit_btn.click()
finally:
    time.sleep(10)
    driver.quit()