"""Created on Fri Apr 30 16:00:37 2021.

@author: Mohammad
"""

import os
import time

from selenium import webdriver

path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, 'chromedriver.exe')
username = 'iamrezamousavi'
password = '1378iamrezamousavi1378'

driver = webdriver.Chrome(executable_path=address)
driver.get('https://instagram.com')

time.sleep(1)

# xpathuser = r"//*[@id="loginForm"]/div/div[1]/div/label/input"
user = driver.find_element_by_css_selector(
    '#loginForm > div > div:nth-child(1) > div > label > input',
)
user.send_keys(username)

# xpathramz = r"//*[@id="loginForm"]/div/div[2]/div/label/input"
ramz = driver.find_element_by_css_selector(
    '#loginForm > div > div:nth-child(2) > div > label > input',
)
ramz.send_keys(password)

time.sleep(2)
# xpathlog = r"//*[@id="loginForm"]/div/div[3]"
driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3)').click()

time.sleep(2)
driver.find_element_by_css_selector(
    '#react-root > section > main > div > div > div > div > button',
).click()


time.sleep(2)
driver.find_element_by_css_selector(
    'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm',
).click()


# driver.quit()
