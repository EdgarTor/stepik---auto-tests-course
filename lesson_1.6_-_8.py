from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(link)

    first_name = driver.find_element(By.NAME, 'first_name')
    first_name.send_keys('Edgar')

    last_name = driver.find_element(By.NAME, 'last_name')
    last_name.send_keys('Torosyan')

    city = driver.find_element(By.NAME, 'firstname')
    city.send_keys('Yerevan')

    country = driver.find_element(By.ID, 'country')
    country.send_keys('Armenia')

    submit_btn = driver.find_element(By.XPATH, '//button[@type = "submit" and text() = "Submit"]')
    submit_btn.click()
finally:
    time.sleep(30)
    driver.quit()