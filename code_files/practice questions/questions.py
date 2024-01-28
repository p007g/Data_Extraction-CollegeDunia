import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import numpy as np
import timeit

# start timer
start_time = timeit.default_timer()

que_link = []
que_txt = []
exam_level_year = []
exam_level = []
que_subject = []
que_title = []

for i in range(1, 1601):
#------getting the URL request----
    user_agents_list = [
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    if(i==1):
        response = requests.get(f'https://collegedunia.com/exams/questions', headers={'User-Agent': random.choice(user_agents_list)})
    else:
        response = requests.get(f'https://collegedunia.com/exams/questions/page-'+str(i), headers={'User-Agent': random.choice(user_agents_list)})
    
    response.raise_for_status()

    #---extracting whole data of URL in HTML format---
    data = BeautifulSoup(response.text, 'lxml')
    
    try:
        #---write code here---
        questions = data.find('div', class_="jsx-867390858 card-body").find_all('div', class_="jsx-4069085995 question-card p-3 mb-3")
        
        for question in questions:
                
            try:
                link = question.find('a').get('href')
                que_link.append(f'https://collegedunia.com{link}')
                
                txt = question.find('div', class_="jsx-3127109378 ck-content").text
                que_txt.append(txt)
                # print(f'https://collegedunia.com{que_link}')
                # print(qtext)
                
                info = question.find_all('li', class_="jsx-4069085995 bg-white rounded py-1 px-2 d-inline-block font-weight-medium text-md")
                que_info = []
                for i in info:
                    que_info.append(i.text)
                    
                exam_level_year.append(que_info[0])
                exam_level.append(que_info[1])
                que_subject.append(que_info[2])
                que_title.append(que_info[3])                
                # print(que_info)
                # print("----------------------------------------------------------------------------------------------")


            except Exception as e:
                print(e)
                
    except Exception as e:
        print(e)
        

try:        
    info = {
        "Que-Link":que_link,
        "Que-Text":que_txt, 
        "Exam Level-Year":exam_level_year,
        "Que-Level":exam_level,
        "Que-Type":que_subject,
        "Que-Title":que_title
        }

    df = pd.DataFrame.from_dict(info, orient='index')
    df = df.transpose()
    df.index = np.arange(1, len(df) + 1)
    # df["Que-No."] = np.arange(1, len(df) + 1)
    # df = df.set_index('Que-No.')
    
except Exception as e:
    print(e)

print(df)

# Save to files------
excel_file = 'extracted_files\practice questions\practice_questions(page#1-1600).xlsx'
df.to_excel(excel_file)



# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")