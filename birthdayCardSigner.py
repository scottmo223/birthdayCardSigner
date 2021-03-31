import time
import urllib.request
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

#hard coded stuff
namesFile = 'birthdayNames.csv'
font = 'Architects Daughter'
username = 'scott.morales@mercyships.org'
myName = 'Scott Morales'
driver = webdriver.Chrome('../chromedriver')  # path to chromedriver.exe

password = input("Password: ")

#login 
driver.get('https://www.openme.com/openme-login')
time.sleep(2)

usernameField = driver.find_element_by_id('edit-name')
passwordField = driver.find_element_by_id('edit-pass')
submitButton = driver.find_element_by_id('edit-submit')

usernameField.clear()
passwordField.clear()

usernameField.send_keys(username)
passwordField.send_keys(password)
submitButton.send_keys(Keys.RETURN)

#open csv file 
with open(namesFile, newline='') as csvfile:
    #save file contents to object
    reader = csv.DictReader(csvfile)

    #cycle through each row and sign the cards
    for row in reader:
        #Set up the greeting
        nameValue = row['firstname']
        url = row['url']
        birthdayGreeting = f"Happy Birthday {nameValue}! I hope it's a good one!"
        
        #go to card url
        driver.get(url)
        #select custom message
        driver.find_element_by_id('write-note-button').send_keys(Keys.RETURN)
        time.sleep(2) #This is necessary for the modal to open up - won't work without it
        #fill out card
        driver.find_element_by_id('edit-message').send_keys(birthdayGreeting)
        driver.find_element_by_id('edit-name').send_keys(myName)
        Select(driver.find_element_by_id('edit-font')).select_by_value('architects_daughter')
        
        #user check - make sure the names match!!! You may have switched them up in the csv file
        procede = input("Procede? y/n: ")
        if(procede == 'y'):
            driver.find_element_by_class_name('submit-button').click()
        else:
            pass

driver.quit()
print('Done!')