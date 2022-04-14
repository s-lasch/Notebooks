import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
import os

global file
file = "C:/Users/steve/Downloads/results.csv"

def get_data():
    # open a Chrome driver
    browser = webdriver.Chrome()

    # go to the login page
    browser.get('https://monkeytype.com/login')

    # enter username
    browser.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/input[1]').send_keys('stevenlasch12@gmail.com')

    # enter password
    browser.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/input[2]').send_keys('hnIkl4432')

    # click sign-in button
    browser.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/div[2]').click()

    try:
        # wait for the page to load
        time.sleep(3)
        
        # remove file if it already exists
        try:
            os.remove(file)
        except Exception:
            pass

        # download CSV data
        browser.find_element_by_xpath('//*[@id="middle"]/div[6]/div[3]/div[12]/div').click()

        # wait for download to complete
        time.sleep(2)
    except Exception as e:
        # raise any exceptions
        raise e

    # close the browser
    browser.close()


def switch_delimiter(filename):
    # convert the pipe delimited csv to a comma delimited csv
    with open(file, "r") as file_pipe:

        # save the new file 
        with open(filename, 'w') as file_comma:
            csv.writer(file_comma, delimiter=',').writerows(csv.reader(file_pipe, delimiter='|'))

