from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

website_link = "yourwebsite"

username = "yourusername"

password = "yourpassword"

element_for_username = "login"
element_for_passowrd = "password"
element_for_submit = "commit"

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
browser.get((website_link))

try:
    username_element = browser.find_element_by_name(element_for_username)
    username_element.send_keys(username)
    password_element = browser.find_element_by_name(element_for_passowrd)
    password_element.send_keys(password)
    loginButton = browser.find_element_by_name(element_for_submit)
    loginButton.click()


	#### to quit the browser  ####
	
    browser.quit()
    time.sleep(1)
    
except Exception:
    print("Some error occured :(")