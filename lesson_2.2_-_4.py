from selenium import webdriver
import time

try:
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://google.com')

    driver.execute_script(
        'document.title = "Script executing";'
        'alert("Robots at work");'
    )
finally:
    time.sleep(5)
    driver.quit()