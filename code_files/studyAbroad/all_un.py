import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import numpy as np


university_country = []
university_name = []
university_place = []
fees = []
top_course = []
exam_score = []

try:
    for i in range(1, 31):
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
                
                try:
                    # 1st block--
                    university_info = university.find('span', class_="jsx-3255989801 flex-fill")

                    name = university_info.find('h3').text
                    university_name.append(name)

                    place = university_info.find('span', class_="jsx-3255989801 text-gray text-md mr-2 text-capitalize").text
                    university_place.append(place)

                    country = university_info.find('span', class_="jsx-3255989801 text-gray text-md mr-2 text-capitalize").text.split(',')[1].strip()
                    university_country.append(country)
                    
                    # 2nd block--
                    tl_fee = university.find('span', class_="jsx-3255989801 col-fees d-flex flex-column")
                    
                    if tl_fee is not None:
                        info = tl_fee.find_all('span', class_="jsx-3255989801 d-flex align-items-baseline mb-1 text-nowrap")
                        
                        tab = {}
                        for i in range(0, len(info)):
                            
                            cond = info[i].find('span', class_="jsx-3255989801 text-black ml-2").text.strip()
                    
                            stat = info[i].find('span', class_="jsx-3255989801 font-weight-bold text-success").text.strip()
                        
                            
                            if cond == 'Tuition:':
                                tab['Tuition'] = stat
                                
                            if cond == 'Living:':
                                tab['Living'] = stat
                                
                                
                        if not tab:
                            fees.append("---")
                        else:
                            fees.append(tab)
                            
                    else:
                        fees.append(None)
                        
                        
                    # 3rd block
                    tc = university.find('span', class_="jsx-3255989801 d-flex flex-column justify-content-between").find('a', class_="jsx-3255989801 text-black font-weight-medium text-lg mb-2")
                    if tc is not None:
                        top_course.append(tc.span.text.strip())
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
                            
                            
                            # ns = []
                            # for score in scores:
                                
                            #     en = score.find('span', class_="jsx-3255989801 text-gray mr-1").text
                            #     es = score.find('span', class_="jsx-3255989801 text-primary font-weight-bold").text
                            #     ns.append(f'{en} - {es}')
                                    
                            
                            # exam_score.append(ns)
                            
                        else:
                            exam_score.append(None)
                        
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
        "Country_Name":university_country,
        "Universities_Name":university_name, 
        "University_Place":university_place,
        "Fees":fees,
        "Top_Course":top_course,
        "Exams_Score":exam_score
        }

    df = pd.DataFrame.from_dict(info, orient='index')
    df = df.transpose()
    # df.index = np.arange(1, len(df) + 1)
    # df["Rank"] = np.arange(1, len(df) + 1)
    
except Exception as e:
    print(e)


# print(len(university_country), len(university_name), len(university_place), len(tuition_fees), len(top_course), len(exam_score))
print(df)


# Save to files------

json_file_path = f'Abroad Universities Data.json'
df.to_json(json_file_path, orient='records')

csv_file_path = f'Abroad Universities Data.csv'
df.to_csv(csv_file_path, index=False)