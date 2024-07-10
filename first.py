from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.binary_location = 'C:/Users/alesk/Desktop/chromedriver-win64/chromedriver.exe'


driver = webdriver.Chrome(options=options)


driver.get('https://web.whatsapp.com')


input("After scanning the QR code, press Enter...")


contact_name = "Username"
message = "Hello World!"
count = 1000

try:

    search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    search_box = driver.find_element(By.XPATH, search_box_xpath)
    search_box.click()
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)

    time.sleep(5)


    message_box_css = 'div[contenteditable="true"][data-tab="10"]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, message_box_css)))
    message_box = driver.find_element(By.CSS_SELECTOR, message_box_css)
    message_box.click()

    for i in range(count):
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(0.1)

finally:

    driver.quit()
