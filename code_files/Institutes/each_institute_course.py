from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import numpy as np
import timeit
import time
import csv
from selenium import webdriver
# import institute_details as id
import institute_course_details as id

# start timer
start_time = timeit.default_timer()


centres = []

try:
    print("loading...")
    for i in range(201, 235):
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
            blocks = data.find('div', class_="jsx-3067688746 row px-0 gap-14").find_all('div', class_="jsx-3067688746 col-12")
            
            for block in blocks:
            
                link = block.find('div', class_="jsx-1571039852 cover-image")
                
                if link is not None:
                    institute_link = link.find('a').get('href')
                    f_institute_link = f'https://collegedunia.com{institute_link}'
                    
                    # finder course details @link---
                    id.getInstituteDetails(f_institute_link)
                    
                    
                center = block.find('div', class_="jsx-1571039852 centers d-flex")
                
                if center is not None:
                    arr = []
                    cn = center.find('span', class_="jsx-1571039852 text-dark f-14 lh-20 font-weight-medium mx-1").text.split(",")
                    for c in range(0, len(cn)):
                        arr.append(cn[c].strip())
                        
                    centres.append(cn)
            

        except Exception as e:
            print(e)
            
except Exception as e:
    print(e)
        
try:        
    fields = {
        "Institute_Name":id.institute_name,
        "Institute_Centres":centres,
        "Institute_Logo":id.institute_logo,
        "Institute_City":id.institute_city,
        "Institute_Rating":id.institute_rating,
        # "Institute_Summary":id.institute_summary,
        "Institute_Type":id.institute_type,
        "Exams/Courses":id.Courses_Name,
        "Course_Fees":id.Courses_Fees,
        "Course_Time":id.Courses_Time,
        "Program_Type":id.Program_Type
        }

    df = pd.DataFrame.from_dict(fields, orient='index')
    df = df.transpose()
    
        
    chunk_size = 300  # Adjust the number of rows per file as needed
    num_chunks = len(df) // chunk_size + (1 if len(df) % chunk_size else 0)

    for i in range(num_chunks):
        new_df = df[i*chunk_size:(i+1)*chunk_size]
        
        # csv_file_path = f'extracted_files\Institute_filtered_data\Institute_data_{i+1}_sample04.csv'
        # new_df.to_csv(csv_file_path, index=False)
        
        json_file_path = f'extracted_files\Institute_filtered_data\Institute_data_{i+21}.json'
        new_df.to_json(json_file_path, orient='records')
        
    # json_file_path = f'extracted_files\Institute_detailed\Institute_data_sample_07.json'
    # df.to_json(json_file_path, orient='records')
    
    # csv_file_path = f'extracted_files\Institute_detailed\Institute_data_sample_03.csv'
    # df.to_csv(csv_file_path, index=False)
        
        
    
except Exception as e:
    print(e)

# print(len(ecd.college_name), len(ecd.college_place), len(ecd.college_approval), len(ecd.college_establishment), len(ecd.college_universityType), len(ecd.college_rating), len(ecd.college_detail))
print(df)


# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")