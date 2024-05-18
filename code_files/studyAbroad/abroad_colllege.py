from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import numpy as np
import timeit
import time
import csv
from selenium import webdriver
import abroad_college_details as ecd

# start timer
start_time = timeit.default_timer()

university_country = []
university_name = []
university_place = []
fees = []
top_course = []
exam_score = []

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
                
                try:
                    # 1st block--
                    university_info = university.find('span', class_="jsx-3255989801 flex-fill")
                    
                    if university_info is not None:

                        name = university_info.find('h3')
                        if name is not None:
                            university_name.append(name.text)

                        place = university_info.find('span', class_="jsx-3255989801 text-gray text-md mr-2 text-capitalize")
                        if place is not None:
                            university_place.append(place.text)

                        country = university_info.find('span', class_="jsx-3255989801 text-gray text-md mr-2 text-capitalize")
                        if country is not None:
                            university_country.append(country.text.split(',')[1].strip().upper())
                    
                    # 2nd block--
                    tl_fee = university.find('span', class_="jsx-3255989801 col-fees d-flex flex-column")
                    
                    if tl_fee is not None:
                        info = tl_fee.find_all('span', class_="jsx-3255989801 d-flex align-items-baseline mb-1 text-nowrap")
                        
                        tab = {}
                        for i in range(0, len(info)):
                            
                            cond = info[i].find('span', class_="jsx-3255989801 text-black ml-2").text.strip()
                    
                            stat = info[i].find('span', class_="jsx-3255989801 font-weight-bold text-success").text.strip()
                        
                            
                            if cond == 'Tuition:':
                                tab['Tuition Fees'] = stat
                                
                            if cond == 'Living:':
                                tab['Living Fees'] = stat
                                
                                
                        if not tab:
                            fees.append("")
                        else:
                            fees.append(tab)
                            
                    else:
                        fees.append(None)
                        
                        
                    # 3rd block
                    tc = university.find('span', class_="jsx-3255989801 d-flex flex-column justify-content-between")
                    if tc is not None:
                        c = tc.find('a', class_="jsx-3255989801 text-black font-weight-medium text-lg mb-2")
                        top_course.append(c.span.text.strip())
                    else:
                        top_course.append(None)
                    
                    
                    try:
                        span = university.find('span', class_="jsx-3255989801 d-flex align-items-center")
                        
                        if span is not None:
                            scores = span.find_all('span', class_="jsx-3255989801 text-md d-flex align-items-center mr-2")
                            
                            es = ""
                            for i in range(0, len(scores)):
                                
                                exam_name = scores[i].find('span', class_="jsx-3255989801 text-gray mr-1").text.strip()
                                score = float(scores[i].find('span', class_="jsx-3255989801 text-primary font-weight-bold").text.strip())
                                
                                es += f'{exam_name}- {score}, '
                                
                                
                            exam_score.append(es.rstrip(", "))
                            
                            
                        else:
                            exam_score.append(None)
                        
                    except:
                        print('')
                    
                except Exception as e:
                    print(e)
                    
                    
                    
                
                # Inner Details---
                
                link = university.find('span', class_="jsx-3255989801 clg-title-wrapper d-flex align-items-start justify-content-start mb-1")
                
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
        "College_Name":university_name,
        "College_Place":university_place,
        "College_Fees":fees,
        "College_Top_Course":top_course,
        "College_Exam_Score":exam_score,
        "College_Heading":ecd.college_heading,
        "College_Logo":ecd.college_logo,
        "Upper_Section_Details":ecd.upper_section_details,
        "College_Rating":ecd.college_rating,
        "College_Summary":ecd.college_summary,
        "Fees_and_Eligibility":ecd.college_fees_eligibility,
        "Courses_Details":ecd.courses_details
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
        
    json_file_path = f'extracted_files\Abroad_datas\Abroad_data_4.json'
    df.to_json(json_file_path, orient='records')
    
    csv_file_path = f'extracted_files\Abroad_datas\Abroad_data_4.csv'
    df.to_csv(csv_file_path, index=False)
        
        
    
except Exception as e:
    print(e)

# print(len(ecd.college_name), len(ecd.college_place), len(ecd.college_approval), len(ecd.college_establishment), len(ecd.college_universityType), len(ecd.college_rating), len(ecd.college_detail))
print(df)


# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")