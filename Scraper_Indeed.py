#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing the necessary Libraries
import pandas as pd
import random
import time
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#Setting Up our webdriver by adding options

chrome_options = Options()

PROXY = "134.238.252.143:8080" #  HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Chrome(executable_path=r'chromedriver', options=chrome_options)

Job_data = []

#Navigationg the links for 20 pages

for page in range(0,210,10):
    
    driver.get(f'https://www.indeed.com/jobs?q=Marketing&l=United+States&sc=0kf%3Ajt%28fulltime%29%3B&radius=50&start={page}')
    time.sleep(random.uniform(8.5, 10.9))
    
    try:
        close = driver.find_element(By.XPATH,'//button[@class = "icl-CloseButton icl-Modal-close"]')
        close.click()  
    except:  
          pass
    
    jobs = driver.find_elements(By.XPATH,'//div[@class = "css-1m4cuuf e37uo190"]')
    
    for job in jobs:
        job.location_once_scrolled_into_view
        job.click()   
        time.sleep(random.uniform(9.6, 10.9))
        
        Job_title = driver.find_element(By.XPATH,'//h1[@class = "icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded"]').text.strip()
        title = Job_title.split('\n')
        Company = driver.find_element(By.XPATH,'//div[@class="jobsearch-InlineCompanyRating icl-u-xs-mt--xs icl-u-xs-mb--md"]').text.strip()
        cmpny = Company.split('\n')
        try: 
            Location = driver.find_element(By.XPATH, '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]').text.strip()
        except:
            Location = 'Remote'
        try:
            Salary = driver.find_element(By.XPATH,'//div[@id = "salaryInfoAndJobType"]').text.strip()
            salary = Salary.split('a')
        except:
            Salary = 'NaN'
            salary = 'None'
        Job_Description = driver.find_element(By.XPATH,'//div[@id = "jobDescriptionText"]').text.strip()
        try:
            Date_Posted = driver.find_element(By.XPATH,'//ul[@class="css-659xjq eu4oa1w0"]').text.strip()
        except:
            Date_Posted = 'NaN'
        data = {'Job Title': title[0],'Company': cmpny[0],'Location': Location,'Salary': salary[0],'Job_Description':Job_Description, 'Date Posted':Date_Posted}
        Job_data.append(data)
        print('[*] Saving')
        
df = pd.DataFrame(Job_data)
df.to_excel('Indeed_Data.xlsx')

