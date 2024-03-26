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


for i in range(201, 234):
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
        universities = data.find('div', class_="jsx-612976036 jsx-3247734209 row mx-n2").find_all('div', class_="jsx-612976036 jsx-3247734209 col-4 pl-0 pr-2 mb-3")


        for university in universities:
            
            try:

                name = university.find('div', class_="jsx-2500342132 clg-name-address").h3.text
                print(name)

                # place = university.find('span', class_="jsx-2500342132 location-badge").text.strip()
                # cleaned_text_place = ''.join([char for char in place if not char.isdigit()])
                # print(cleaned_text_place.strip())
                
                logo = university.find('div', class_="jsx-2500342132 clg-logo bg-white").find('img')
                logo_url = logo.get('data-src')
                # print(logo_url)
                
                # # Check if the image URL is complete; if not, append the base URL
                # if not image_url.startswith('http'):
                #     image_url = url + image_url
                
                img_name = f"extracted_files\Institutes Data\institute_logo_05\{name}_logo.jpg"
                logo_data =requests.get(logo_url).content
                with open(img_name, 'wb') as handler:
                    handler.write(logo_data)

                # print("...........")
                
            except Exception as e:
                print(e)
                

    except Exception as e:
        print(e)
        
# try:        
#     info = {
#         "Country":university_country,
#         "Universities Names":university_name, 
#         "University Place":university_place,
#         "Tuition Fees":tuition_fees,
#         "Living Fees":living_fees,
#         "Top Course":top_course
#         }

#     df = pd.DataFrame.from_dict(info, orient='index')
#     df = df.transpose()
#     df.index = np.arange(1, len(df) + 1)
#     # df["Rank"] = np.arange(1, len(df) + 1)
    
# except Exception as e:
#     print(e)

# # print(len(university_country), len(university_name), len(university_place), len(tuition_fees), len(living_fees))
# print(df)

# Save to files------
# excel_file = 'Abroad Universities(living-fees) Data.xlsx'
# df.to_excel(excel_file, sheet_name='All Universities')