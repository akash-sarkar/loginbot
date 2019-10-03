#By Akash Sarkar
#Gmail Login Bot

from selenium import webdriver
import time

username=input("Give the Email address or username= ")
password=input("Give the password= ")
print("Request Processing.............")
url='https://gmail.com'
driver=webdriver.Firefox()
driver.get(url)

driver.find_element_by_id('identifierId').send_keys(username)
time.sleep(2)
driver.find_element_by_id('identifierNext').click()
time.sleep(1.5)
driver.find_element_by_name('password').send_keys(password)
time.sleep(2)
driver.find_element_by_id('passwordNext').click()
time.sleep(1.5)