from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('no-sandbox')



def login(driver, email, password):
    driver.get("http://www.okey.xyz/login")
    time.sleep(2)

    # login to masterqr
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("waves-light").click()
    driver.find_element_by_link_text("Update Your Smart Card").click()
    driver.find_element_by_name("first_name").send_keys(' Ahmed')
    driver.find_element_by_name("last_name").send_keys(' bappy')
    driver.find_element_by_link_text("Update").click()

    time.sleep(2)

email = "taj@gmail.com"
password = "12345dd678"

driver = webdriver.Chrome(executable_path=r'/home/bappy/www/python/scraping/chromedriver', options=options)
login(driver, email, password)