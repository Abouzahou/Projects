from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_browser = webdriver.Chrome(options=options)


chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
button = chrome_browser.find_element("name", "btn-primary")

print(button)

time.sleep(5000)