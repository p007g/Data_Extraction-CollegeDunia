from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import numpy as np
import timeit
import csv
from selenium import webdriver
import acd

# start timer
start_time = timeit.default_timer()


try:
    print("loading...")
    for i in range(11, 15):
        #------getting the URL request----
        user_agents_list = [
        'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        if(i==1):
            response = requests.get(f'https://collegedunia.com/study-abroad-universities', headers={'User-Agent': random.choice(user_agents_list)})
        else:
            response = requests.get(f'https://collegedunia.com/study-abroad-universities/page-'+str(i), headers={'User-Agent': random.choice(user_agents_list)})

        response.raise_for_status()


        #---extracting whole data of URL in HTML format---
        data = BeautifulSoup(response.text, 'lxml')
        
        try:
        #---write code here---
            universities = data.find('tbody', class_="jsx-4182613765").find_all('tr', class_="jsx-3255989801 automate_client_img_snippet")

            for university in universities:
                
                # Outer Details----
                
                
                
                # Inner Details---
                
            
                link = university.find('span', class_="jsx-3255989801 clg-title-wrapper d-flex align-items-start justify-content-start mb-1")
                # print(link)
                
                if link is not None:
                    un_link = link.find('a').get('href')
                    f_un_link = f'https://collegedunia.com{un_link}'
                    # print(f_un_link)
                    
                    # finder course details @link---
                    acd.getAbroadDetails(f_un_link)
                    
                    # course fees and eligibility---
                    # ecd.getfees(f_college_link)
                    
                    
                # centres = block.find('div', class_="jsx-2127947714 centers d-flex")
                
                # if centres is not None:
                #     cn = centres.find('span', class_="jsx-2127947714 text-dark f-14 lh-20 font-weight-medium mx-1").text
                #     print(cn)
                
                
                print("------------------------------------------------------------")                
            

        except Exception as e:
            print(e)
            
except Exception as e:
    print(e)
    
        
# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")