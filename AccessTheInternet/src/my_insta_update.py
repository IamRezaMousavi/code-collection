"""Created on Sat May  1 06:30:06 2021

@author: Mohammad
"""

import os
import time

from selenium import webdriver

path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, 'chromedriver.exe')
username = 'thecleverking1'
password = '13781378'
tegs = '#london'

driver = webdriver.Chrome(executable_path=address)
driver.get('https://instagram.com')
time.sleep(1)

user = driver.find_element_by_css_selector(
    '#loginForm > div > div:nth-child(1) > div > label > input',
)
user.send_keys(username)

ramz = driver.find_element_by_css_selector(
    '#loginForm > div > div:nth-child(2) > div > label > input',
)
ramz.send_keys(password)

driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3)').click()

# time.sleep(3)
search = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input',
)
search.send_keys(tegs)

time.sleep(3)
driver.find_element_by_xpath('//a[@class="-qQT3"]').click()

# driver.quit()
