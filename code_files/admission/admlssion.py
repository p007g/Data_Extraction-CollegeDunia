from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import numpy as np
import timeit
import time
import csv
from selenium import webdriver
import admission_details as ad

# start timer
start_time = timeit.default_timer()

# university_country = []
# university_name = []
# university_place = []
# fees = []
# top_course = []
# exam_score = []

college_logo = []
application_date = []
course_name = []
clg_name = []

try:
    print("loading...")
    for i in range(7, 11):
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
                    
                    logo = university.find('a', class_="jsx-2397409965 text-decoration-none image-wrap d-block")
                    if logo is not None:
                        url = logo.find('img').get('data-src')
                        college_logo.append(url)
                    
                    university_info = university.find('div', class_="jsx-2397409965 detail p-2")
                    
                    if university_info is not None:

                        app_date = university_info.find('span', class_="jsx-2397409965 text-silver font-weight-bold text-sm")
                        if app_date is not None:
                            application_date.append(app_date.text)
                            
                        cn = university_info.find('span', class_="jsx-2397409965 text-secondary d-block py-1 text-sm font-weight-bold")
                        if cn is not None:
                            course_name.append(cn.text)
                        else:
                            course_name.append("")
                            
                        name = university_info.find('h3', class_="jsx-2397409965 title font-weight-bolder mt-2")
                        if name is not None:
                            clg_name.append(name.text)
                            
                    
                except Exception as e:
                    print(e)
                    
                    
                    
                # Inner Details---
                
                link = university.find('div', class_="jsx-2397409965 detail p-2")
                
                if link is not None:
                    un_link = link.find('a').get('href')
                    f_un_link = f'https://collegedunia.com{un_link}'
                    # print(f_un_link)
                    
                    # finder course details @link---
                    ad.getAdmissionDetails(f_un_link)
                    

        except Exception as e:
            print(e)
            
except Exception as e:
    print(e)
        
try:        
    fields = {
        "College Name": clg_name,
        "College Logo": college_logo,
        "Course Name": course_name,
        "Application Date": application_date,
        "College Location":ad.clg_location,
        "College Afilliation":ad.affiliation,
        "College Info":ad.college_info
        }

    df = pd.DataFrame.from_dict(fields, orient='index')
    df = df.transpose()
    
        
    # chunk_size = 300  # Adjust the number of rows per file as needed
    # num_chunks = len(df) // chunk_size + (1 if len(df) % chunk_size else 0)

    # for i in range(num_chunks):
    #     new_df = df[i*chunk_size:(i+1)*chunk_size]
        
    #     # csv_file_path = f'extracted_files\statewise_colleges\{state}_data_{i+1}.csv'
    #     # new_df.to_csv(csv_file_path, index=False)
        
    #     json_file_path = f'extracted_files\Institute_detailed_data\Institute_data_{i+11}.json'
    #     new_df.to_json(json_file_path, orient='records')
        
    json_file_path = f'extracted_files\Admission Data\Admission_sp1.json'
    df.to_json(json_file_path, orient='records')
    
    csv_file_path = f'extracted_files\Admission Data\Admission_sp1.csv'
    df.to_csv(csv_file_path, index=False)
        
        
    
except Exception as e:
    print(e)

# print(len(ecd.college_name), len(ecd.college_place), len(ecd.college_approval), len(ecd.college_establishment), len(ecd.college_universityType), len(ecd.college_rating), len(ecd.college_detail))
print(df)


# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")