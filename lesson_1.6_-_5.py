from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/find_link_text'
url_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    a = driver.find_element(By.LINK_TEXT, url_text)
    a.click()

    first_name = driver.find_element(By.NAME, 'first_name')
    first_name.send_keys('Edgar')

    last_name = driver.find_element(By.NAME, 'last_name')
    last_name.send_keys('Torosyan')

    city = driver.find_element(By.CSS_SELECTOR, 'div.form-group input.city')
    city.send_keys('Yerevan')

    country = driver.find_element(By.ID, 'country')
    country.send_keys('Armenia')

    submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()
finally:
    time.sleep(30)
    driver.quit()
