"""Created on Fri Apr 30 16:00:37 2021

@author: Mohammad
"""

import os
import time

from selenium import webdriver

path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, 'chromedriver.exe')
username = 'thecleverking1'
password = '13781378'

driver = webdriver.Chrome(executable_path=address)
driver.get('https://instagram.com')


user = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
user.send_keys(username)

ramz = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
ramz.send_keys(password)

time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()


# driver.quit()
