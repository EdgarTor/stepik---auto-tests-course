from selenium import webdriver
import time

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    time.sleep(5)

    driver.get('https://stepik.org/lesson/25969/step/12')
    time.sleep(5)

    textarea = driver.find_element_by_css_selector('.textarea')
    textarea.send_keys('get()')
    time.sleep(5)

    submit_button = driver.find_element_by_css_selector('.submit-submission')
    submit_button.click()
    time.sleep(5)
finally:
    driver.quit()
