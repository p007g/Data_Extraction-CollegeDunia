import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import numpy as np
import timeit

# start timer
start_time = timeit.default_timer()


scholarship_name = []
scholarship_eligibility = []
scholarship_amount = []
scholarship_type = []
scholarship_study_level = []
no_of_scholarships = []

for i in range(1, 30):
#------getting the URL request----
    user_agents_list = [
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    if(i==1):
        response = requests.get(f'https://collegedunia.com/scholarship', headers={'User-Agent': random.choice(user_agents_list)})
    else:
        response = requests.get(f'https://collegedunia.com/scholarship/page-'+str(i), headers={'User-Agent': random.choice(user_agents_list)})
    
    response.raise_for_status()

    #---extracting whole data of URL in HTML format---
    data = BeautifulSoup(response.text, 'lxml')
    
    try:
        #---write code here---
        cards = data.find('div', class_="jsx-4142307919 jsx-3247734209 row").find_all('div', class_="jsx-2004262814 col-4 scholarship-card mb-4")
        
        for card in cards:
                
            try:
                title = card.find('h2', class_="jsx-2004262814 m-0 scholar-card-heading p-3 text-truncate").text
                scholarship_name.append(title)
                
                info = card.find('ul').find_all('li', class_="jsx-2004262814 pb-3 text-lg")
                scholar_info = []
                for l in info:
                    scholar_info.append(l.span.text)
                    
                scholarship_eligibility.append(scholar_info[0])
                scholarship_amount.append(scholar_info[1])
                scholarship_type.append(scholar_info[2])
                scholarship_study_level.append(scholar_info[3])
                no_of_scholarships.append(scholar_info[4])           
                

            except Exception as e:
                print(e)
                
    except Exception as e:
        print(e)
        

try:        
    fields = {
        "Scholarship Name":scholarship_name,
        "International Student Eligibility":scholarship_eligibility, 
        "Amount":scholarship_amount,
        "Type of Scholarship":scholarship_type,
        "Level of Study":scholarship_study_level,
        "No. of Scholarships":no_of_scholarships
        }

    df = pd.DataFrame.from_dict(fields, orient='index')
    df = df.transpose()
    df.index = np.arange(1, len(df) + 1)
    # df["Sr-No"] = np.arange(1, len(df) + 1)
    # df = df.set_index('Sr-No')
    
except Exception as e:
    print(e)

print(df)

# Save to files------
excel_file = 'extracted_files\scholarship_data.xlsx'
df.to_excel(excel_file)



# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")