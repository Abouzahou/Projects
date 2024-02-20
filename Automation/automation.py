from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_browser = webdriver.Chrome(options=options)


chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')

#print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_button2 = chrome_browser.find_element(By.CSS_SELECTOR, '#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('This is a test Input')

show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')

assert 'This is a test Input' in output_message.text

#time.sleep(5000)

chrome_browser.quit()