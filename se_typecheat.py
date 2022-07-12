from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

driverPath = os.path.abspath('chromedriver')
driver = webdriver.Chrome(driverPath)
driver.get('https://play.typeracer.com/')

driver.implicitly_wait(10)

raceButton = driver.find_element(By.LINK_TEXT, 'Enter a Typing Race')
raceButton.click()


