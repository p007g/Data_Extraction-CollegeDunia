import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import numpy as np



exam = []
exam_name = []
exam_detail = []
mode = []
living_fees = []


for i in range(1, 2):
    #------getting the URL request----
    user_agents_list = [
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    response = requests.get(f'https://collegedunia.com/exams/study-abroad-exams', headers={'User-Agent': random.choice(user_agents_list)})

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

                tuition = university.find('span', class_="jsx-3255989801 col-fees d-flex flex-column").text.split()[1]
                if tuition.startswith("₹"):
                    tuition_fees.append(tuition)
                else:
                    tuition_fees.append('NA')
                

                living = university.find('span', class_="jsx-3255989801 col-fees d-flex flex-column").text.split()[3]
                if living.startswith("₹"):
                    living_fees.append(living)
                else:
                    living_fees.append('NA')
                    
                
                top_course = university.find
                    
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
        "Living Fees":living_fees
        }

    df = pd.DataFrame.from_dict(info, orient='index')
    df = df.transpose()
    df.index = np.arange(1, len(df) + 1)
    # df["Rank"] = np.arange(1, len(df) + 1)
    
except Exception as e:
    print(e)

# print(len(university_country), len(university_name), len(university_place), len(tuition_fees), len(living_fees))
print(df)

# Save to files------
excel_file = 'Abroad Universities(living-fees) Data.xlsx'
df.to_excel(excel_file, sheet_name='All Universities')