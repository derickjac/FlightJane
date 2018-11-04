from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re


#driver = webdriver.Chrome()
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/Users/derickjacquez/Desktop"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "/Users/derickjacquez/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)


origin = "houston"
depart = "boston"

driver.get("https://google.com")
search = driver.find_element_by_name('q')
search.send_keys(origin, " to ", depart, " cheap flight")
search.submit()

pageSource = str(driver.page_source)
bsObj = BeautifulSoup(pageSource)
output = bsObj.find("div", {"id": "flt"})
#output = output.find()
output = output.find("div", {"class": "flt-results"})
output = output.find("span", {"class": "cUntLb"})
#output = output.findall(text=True, recursive=False)
print(output)