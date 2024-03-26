import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import numpy as np


university_country = []
university_name = []
university_place = []
tuition_fees = []
living_fees = []
top_course = []
exam_score = []

try:
    for i in range(1, 40):
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
            universities = data.find('tbody', class_="jsx-1597785535").find_all('tr', class_="jsx-3255989801 automate_client_img_snippet")


            for university in universities:
                
                try:
                    university_info = university.find('span', class_="jsx-3255989801 flex-fill")

                    name = university_info.find('h3').text
                    university_name.append(name)

                    place = university_info.find('span', class_="jsx-3255989801 text-gray text-md mr-2 text-capitalize").text
                    university_place.append(place)

                    country = university_info.find('span', class_="jsx-3255989801 text-gray text-md mr-2 text-capitalize").text.split(',')[1]
                    university_country.append(country)

                    tuition = university.find('span', class_="jsx-3255989801 col-fees d-flex flex-column")
                    t = tuition.text.split()[1]
                    if t.startswith("₹") and tuition is not None:
                        tuition_fees.append(tuition.text.split()[1])
                    else:
                        tuition_fees.append('')
                    

                    living = university.find('span', class_="jsx-3255989801 col-fees d-flex flex-column")
                    l = living.text.split()[3]
                    if l.startswith("₹") and living is not None:
                        living_fees.append(living.text.split()[3])
                    else:
                        living_fees.append('')
                        
                    
                    tc = university.find('span', class_="jsx-3255989801 d-flex flex-column justify-content-between")
                    if tc is not None:
                        top_course.append(tc.a.span.text.strip())
                    else:
                        top_course.append('')
                    
                    try:
                        scores = university.find('span', class_="jsx-3255989801 d-flex align-items-center").find_all('span', class_="jsx-3255989801 text-md d-flex align-items-center mr-2")
                        
                        ns = []
                        for score in scores:
                            en = score.find('span', class_="jsx-3255989801 text-gray mr-1").text
                            es = score.find('span', class_="jsx-3255989801 text-primary font-weight-bold").text
                            ns.append(f'{en} - {es}')
                        
                        exam_score.append(ns)
                        
                    except:
                        print('')
                    
                except Exception as e:
                    print(e)
                    

        except Exception as e:
            print(e)
            
except Exception as e:
    print(e)
        
try:        
    info = {
        "Country":university_country,
        "Universities Names":university_name, 
        "University Place":university_place,
        "Tuition Fees":tuition_fees,
        "Living Fees":living_fees,
        "Top Course":top_course,
        "Exam Score":exam_score
        }

    df = pd.DataFrame.from_dict(info, orient='index')
    df = df.transpose()
    # df.index = np.arange(1, len(df) + 1)
    # df["Rank"] = np.arange(1, len(df) + 1)
    
except Exception as e:
    print(e)

# print(len(university_country), len(university_name), len(university_place), len(tuition_fees), len(living_fees))
# print(df)

# Save to files------
excel_file = 'Abroad Universities all Data.csv'
df.to_csv(excel_file)