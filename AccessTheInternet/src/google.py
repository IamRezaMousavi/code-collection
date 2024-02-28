"""Created on Sat May  1 04:23:31 2021

@author: Mohammad
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, "chromedriver.exe")
word = input("What you want to search?")

driver = webdriver.Chrome(executable_path=address)
driver.get("https://google.com")

time.sleep(1)

search = driver.find_element_by_css_selector(
    "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input"
)
search.send_keys(word)
search.send_keys(Keys.ENTER)
