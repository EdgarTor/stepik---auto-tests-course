from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/wait1.html'

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(link)

    verify_btn = driver.find_element(By.ID, 'verify')
    verify_btn.click()

    succes_msg = driver.find_element(By.ID, 'verify_message')

    assert 'Verification was successful!' in succes_msg.text
finally:
    time.sleep(5)
    driver.quit()