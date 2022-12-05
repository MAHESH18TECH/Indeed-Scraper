#!/usr/bin/env python
# coding: utf-8

# In[28]:


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

chrome_options = Options()

PROXY = "134.238.252.143:8080" #  HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Chrome(executable_path=r'chromedriver', options=chrome_options)



for page in range(0,50,10):
    
    driver.get(f'https://in.indeed.com/jobs?q=Data+Scientist&l=Pune&start={page}')
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
        time.sleep(random.uniform(4.6, 6.9))
        
        Job_title = driver.find_element(By.XPATH,'//h1[@class = "icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded"]').text.strip()
        title = Job_title.split('\n')
        Company = driver.find_element(By.XPATH,'//div[@class="jobsearch-InlineCompanyRating icl-u-xs-mt--xs icl-u-xs-mb--md"]').text.strip()
        cmpny = Company.split('\n')
        Location = driver.find_element(By.XPATH, "//div[@class[string-length()=0]]").text.strip()
        loc = Location.split('\n')
        try:
            Salary = driver.find_element(By.XPATH,'//div[@id = "salaryInfoAndJobType"]').text.strip()
            salary = Salary.split('a')
        except:
            Salary = 'NaN'
        Job_Description = driver.find_element(By.XPATH,'//div[@id = "jobDescriptionText"]').text.strip()
        Job_data = []
        data = {'Job_Title': title[0],'Company': cmpny[0],'Location': loc[3],'Salary': salary[0],'Job_Description':Job_Description}
        Job_data = []
        Job_data.append(data)
        print('[*] Saving')
        
df = pd.DataFrame(Job_data)
df
df.to_excel('Indeed_JobData2.xlsx')


# In[6]:


data


# In[11]:


jobs


# In[24]:


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

chrome_options = Options()

PROXY = "134.238.252.143:8080" #  HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Chrome(executable_path=r'chromedriver', options=chrome_options)



for page in range(0,10,10):
    
    driver.get(f'https://in.indeed.com/jobs?q=Data+Scientist&l=Pune&start={page}')
    
    try:
        close = driver.find_element(By.XPATH,'//button[@class = "icl-CloseButton icl-Modal-close"]')
        close.click()  
    except:  
          pass
    
    jobs = driver.find_elements(By.XPATH,'//div[@class = "css-1m4cuuf e37uo190"]')
    
    print(len(jobs))
    
    for job in jobs:
        job.location_once_scrolled_into_view
        job.click()
        time.sleep(random.uniform(2.5, 4.9))
        print('Job found')
        


# In[ ]:


jobTitle css-1h4a4n5 eu4oa1w0 jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0

