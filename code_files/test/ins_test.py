from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import numpy as np
import timeit
import time
import csv
from selenium import webdriver
import ins_details_test as id

# start timer
start_time = timeit.default_timer()


try:
    print("loading...")
    for i in range(1, 2):
        #------getting the URL request----
        user_agents_list = [
        'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        if(i==1):
            response = requests.get(f'https://collegedunia.com/institutes', headers={'User-Agent': random.choice(user_agents_list)})
        else:
            response = requests.get(f'https://collegedunia.com/institutes/page-'+str(i), headers={'User-Agent': random.choice(user_agents_list)})

        response.raise_for_status()


        #---extracting whole data of URL in HTML format---
        data = BeautifulSoup(response.text, 'lxml')
        
        try:
        #---write code here---
            blocks = data.find('div', class_="jsx-3117672527 row px-0 gap-14").find_all('div', class_="jsx-3117672527 col-12")
            
            for block in blocks:
            
                link = block.find('div', class_="jsx-2127947714 cover-image")
                # print(link)
                
                if link is not None:
                    institute_link = link.find('a').get('href')
                    f_institute_link = f'https://collegedunia.com{institute_link}'
                    print(f_institute_link)
                    
                    # finder course details @link---
                    id.getInstituteDetails(f_institute_link)
                    
                    # course fees and eligibility---
                    # ecd.getfees(f_college_link)
                    
                    
                centres = block.find('div', class_="jsx-2127947714 centers d-flex")
                
                if centres is not None:
                    cn = centres.find('span', class_="jsx-2127947714 text-dark f-14 lh-20 font-weight-medium mx-1").text
                    print(cn)
                
                
                print("--------------------------------")                    
            

        except Exception as e:
            print(e)
            
except Exception as e:
    print(e)
    
        
# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")