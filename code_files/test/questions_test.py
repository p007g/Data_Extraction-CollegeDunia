import requests
from bs4 import BeautifulSoup
import random



for i in range(1, 2):
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
                
                que_link = question.find('a').get('href')
                que_text = question.find('div', class_="jsx-3127109378 ck-content").text
                # print(f'https://collegedunia.com{que_link}')
                # print(qtext)
                
                info = question.find_all('li', class_="jsx-4069085995 bg-white rounded py-1 px-2 d-inline-block font-weight-medium text-md")
                que_info = []
                for i in info:
                    que_info.append(i.text)
                
                print(que_info[3])                  
                # print(que_info)
                # print("----------------------------------------------------------------------------------------------")


            except Exception as e:
                print(e)
                
    except Exception as e:
        print(e)