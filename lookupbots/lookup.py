# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 02:07:08 2023

@author: c.samanja09
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
driver = webdriver.Chrome()
url1='https://therealdeal.com/'
driver.get("https://www.linkedin.com/")
time.sleep(3)
driver.maximize_window()

email=driver.find_element(By.ID,"session_key")
password = driver.find_element(By.ID,"session_password")
submit = driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/section[1]/div[1]/div[1]/form[1]/div[2]/button[1]")
email.send_keys("Michael.Levy@GrandLuxRealty.com")
password.send_keys("GrandLuxRealty1!")
submit.click()
time.sleep(10)


driver.get('https://www.linkedin.com/search/results/people/?keywords=chappaqua%20real%20estate&origin=SWITCH_SEARCH_VERTICAL&sid=ixb')
time.sleep(10)
j= 1
while j < 100:
  time.sleep(10)

  for i in range(0,10):
        lists=driver.find_elements(By.CLASS_NAME,"reusable-search__result-container")
        if i > 0 :
           driver.execute_script("arguments[0].scrollIntoView(true);", lists[i-1])
        time.sleep(5)
        lists[i].click()
    
        time.sleep(5)
        try:
           driver.execute_script("document.activeElement") 
    
           driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']").click()
        except:
            time.sleep(5)
            driver.back()
        time.sleep(5)

  j=j+1
  print(j)
  driver.execute_script("window.scrollBy(0,600)", "")
  time.sleep(10)
  next=driver.find_element(By.XPATH,"//button[@aria-label='Next']")
  next.click()


   
