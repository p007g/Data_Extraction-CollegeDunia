from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import numpy as np
import timeit
import time
import csv
from selenium import webdriver
import abroad_course_details as ecd

# start timer
start_time = timeit.default_timer()

university_country = []
university_name = []
university_place = []
# fees = []
# top_course = []
# exam_score = []

try:
    print("loading...")
    for i in range(31, 36):
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
            universities = data.find('tbody', class_="jsx-4182613765").find_all('tr', class_="jsx-3040859135 automate_client_img_snippet")

            for university in universities:
                
                # Outer Details----
                
                try:
                    # 1st block--
                    university_info = university.find('span', class_="jsx-3040859135 flex-fill")
                    
                    if university_info is not None:

                        name = university_info.find('h3')
                        if name is not None:
                            university_name.append(name.text)

                        place = university_info.find('span', class_="jsx-3040859135 text-gray text-md mr-2 text-capitalize")
                        if place is not None:
                            university_place.append(place.text.split(',')[0].strip())

                        country = university_info.find('span', class_="jsx-3040859135 text-gray text-md mr-2 text-capitalize")
                        if country is not None:
                            university_country.append(country.text.split(',')[1].strip().upper())
                    
                    
                except Exception as e:
                    print(e)
                    
                    
                # Inner Details---
                
                link = university.find('span', class_="jsx-3040859135 clg-title-wrapper d-flex align-items-start justify-content-start mb-1")
                
                if link is not None:
                    un_link = link.find('a').get('href')
                    f_un_link = f'https://collegedunia.com{un_link}'
                    # print(f_un_link)
                    
                    # finder course details @link---
                    ecd.getAbroadDetails(f_un_link)
                    

        except Exception as e:
            print(e)
            
except Exception as e:
    print(e)
        
try:        
    fields = {
        "College_Country_Name":university_country,

        "College_City":university_place,
        "College_Name":university_name,
        # "College_Fees":fees,
        # "College_Top_Course":top_course,
        # "College_Exam_Score":exam_score,
        # "College_Heading":ecd.college_heading,
        "College_Logo":ecd.college_logo,
        # "Upper_Section_Details":ecd.upper_section_details,
        "College_Rating":ecd.college_rating,
        "Courses":ecd.Courses_name,
        "Courses Years":ecd.Courses_year,
        "Courses Degree":ecd.Courses_degree,
        "Courses Languages":ecd.Courses_grad,
        "Courses Timing":ecd.Courses_time,
        "Courses Fees":ecd.Courses_fees
        # "College_Summary":ecd.college_summary,
        # "Fees_and_Eligibility":ecd.college_fees_eligibility,
        # "Courses_Details":ecd.courses_details
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
        
    json_file_path = f'extracted_files\study_abroad_courses\Abroad_courses_4.json'
    df.to_json(json_file_path, orient='records')
    
    # csv_file_path = f'extracted_files\study_abroad_courses\Abroad_courses_1.csv'
    # df.to_csv(csv_file_path, index=False)
        
        
    
except Exception as e:
    print(e)

# print(len(ecd.college_name), len(ecd.college_place), len(ecd.college_approval), len(ecd.college_establishment), len(ecd.college_universityType), len(ecd.college_rating), len(ecd.college_detail))
print(df)


# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")