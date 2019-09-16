from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/registration1.html'

try:
    driver = webdriver.Chrome('..//drivers/chromedriver.exe')
    driver.get(link)

    first_name = driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "Input your first name"]')
    first_name.send_keys('Edgar')

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "Input your last name"]')
    last_name.send_keys('Torosyan')

    email = driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "Input your email"]')
    email.send_keys('example@mail.com')

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type = submit]')
    submit_btn.click()
    time.sleep(3)

    succes_msg = driver.find_element(By.TAG_NAME, 'h1')
    succes_msg_text = succes_msg.text

    assert 'Congratulations! You have successfully registered!' == succes_msg_text
finally:
    time.sleep(10)
    driver.quit()