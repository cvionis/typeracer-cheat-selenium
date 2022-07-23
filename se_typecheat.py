from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

wpm_input = input('Enter a typing speed for the script:\n> ')

driver_path = os.path.abspath('chromedriver')
driver = webdriver.Chrome(driver_path)
driver.get('https://play.typeracer.com/')

driver.implicitly_wait(10)

race_button = driver.find_element(By.LINK_TEXT, 'Enter a Typing Race')
race_button.click()

prompt_text = (driver.find_element(By.CLASS_NAME, 'inputPanel')).text

# remove extra string following prompt text ('change display format')
print('\n' + prompt_text.replace('change display format', ''))

pt_words = prompt_text.split()

text_input = driver.find_element(By.CLASS_NAME, 'txtInput')
game_status = driver.find_element(By.CLASS_NAME, 'gameStatusLabel')

try:
    while True:
        if game_status.text == 'The race is on! Type the text below:':
            for word in pt_words:
                text_input.send_keys(word + ' ')
                time.sleep(0.25)
        if game_status.text == 'The race has ended.' or 'You finished' in game_status.text:
            break
except:
    driver.quit()
        
    


