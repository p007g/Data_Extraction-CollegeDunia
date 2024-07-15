from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import numpy as np
import timeit
import csv
from selenium import webdriver
import admission_test_details

# start timer
start_time = timeit.default_timer()


try:
    print("loading...")
    for i in range(1, 3):
        #------getting the URL request----
        user_agents_list = [
        'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        if(i==1):
            response = requests.get(f'https://collegedunia.com/admission', headers={'User-Agent': random.choice(user_agents_list)})
        else:
            response = requests.get(f'https://collegedunia.com/admission/'+str(i), headers={'User-Agent': random.choice(user_agents_list)})

        response.raise_for_status()


        #---extracting whole data of URL in HTML format---
        data = BeautifulSoup(response.text, 'lxml')
        
        try:
        #---write code here---
            universities = data.find('div', class_="jsx-118875584 row").find_all('div', class_="jsx-2397409965 col-3 mb-6")

            for university in universities:
                
                # Outer Details----
                
                try:
                    # 1st block--
                    # print(university)
                    logo = university.find('a', class_="jsx-2397409965 text-decoration-none image-wrap d-block")
                    if logo is not None:
                        url = logo.find('img').get('data-src')
                        print(url)
                    
                    university_info = university.find('div', class_="jsx-2397409965 detail p-2")
                    
                    if university_info is not None:
                        
                        app_date = university_info.find('span', class_="jsx-2397409965 text-silver font-weight-bold text-sm")
                        if app_date is not None:
                            print(app_date.text)
                            
                        course_name = university_info.find('span', class_="jsx-2397409965 text-secondary d-block py-1 text-sm font-weight-bold")
                        if course_name is not None:
                            print(course_name.text)
                        else:
                            print("")
                            
                        name = university_info.find('h3', class_="jsx-2397409965 title font-weight-bolder mt-2")
                        if name is not None:
                            print(name.text)

                    
                except Exception as e:
                    print(e)
                
                
                # Inner Details---
                
            
                link = university.find('div', class_="jsx-2397409965 detail p-2")
                # print(link)
                
                if link is not None:
            #         # university_name = link.find('h3', class_="jsx-3040859135 mb-0 d-inline").text.strip()
            #         # print(university_name)
                    
                    un_link = link.find('a').get('href')
                    f_un_link = f'https://collegedunia.com{un_link}'
                    print(f_un_link)
                    
                    # finder course details @link---
                    admission_test_details.getAdmissionDetails(f_un_link)
                    
                
                print("------------------------------------------------------------")                
            

        except Exception as e:
            print(e)
            
except Exception as e:
    print(e)
    
        
# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")