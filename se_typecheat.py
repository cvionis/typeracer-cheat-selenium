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

promptText = (driver.find_element(By.CLASS_NAME, 'inputPanel')).text

# Remove extra string following prompt text ('change display format')
print(promptText.replace('change display format', ''))

ptWords = promptText.split()

textInput = driver.find_element(By.CLASS_NAME, 'txtInput')

gameStatus = driver.find_element(By.CLASS_NAME, 'gameStatusLabel')

try:
    while True:
        if gameStatus.text == 'The race is on! Type the text below:':
            for word in ptWords:
                textInput.send_keys(word + ' ')
                time.sleep(0.25)
        if gameStatus.text == 'The race has ended.' or 'You finished' in gameStatus.text:
            break
except:
    driver.quit()
        
    


