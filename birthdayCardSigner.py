import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import urllib.request
import csv

namesFile = 'birthdayNames.csv'
font = 'Architects Daughter'
username = 'scott.morales@mercyships.org'
password = input("Password: ")
myName = 'Scott Morales'

driver = webdriver.Chrome('../chromedriver')  # path to chromedriver.exe
driver.get('https://www.openme.com/openme-login')

time.sleep(2)

#login 
usernameField = driver.find_element_by_id('edit-name')
passwordField = driver.find_element_by_id('edit-pass')
submitButton = driver.find_element_by_id('edit-submit')

usernameField.clear()
passwordField.clear()
usernameField.send_keys(username)
passwordField.send_keys(password)
time.sleep(2)

submitButton.send_keys(Keys.RETURN)

#open file 
with open(namesFile, newline='') as csvfile:
    #save file contents to object
    reader = csv.DictReader(csvfile)

    #insert file object contents into string template
    for row in reader:
        #Set up sql string template
        nameValue = row['firstname']
        url = row['url']
        birthdayGreeting = f"Happy Birthday {nameValue}! I hope it's a good one!"
        driver.get(url)
        driver.find_element_by_id('write-note-button').send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_id('edit-message').send_keys(birthdayGreeting)
        driver.find_element_by_id('edit-name').send_keys(myName)
        Select(driver.find_element_by_id('edit-font')).select_by_value('architects_daughter')
        
        procede = input("Procede? y/n: ")
        if(procede == 'y'):
            driver.find_element_by_class_name('submit-button').click()
        else:
            pass
        


print('Done!')

driver.quit()