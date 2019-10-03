#By Akash Sarkar
#Gmail Login Bot

from selenium import webdriver
import time
import getpass

def driver(username,password):
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
    

u=input("Give the Email address or username= ")
p = getpass.getpass('Password= ')
print("Request Processing.............")
driver(u,p)
