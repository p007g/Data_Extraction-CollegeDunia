import requests
from bs4 import BeautifulSoup
import random


class Scholarship:
    

    # class default method------
    def __init__(self, country_name):
        # self.country_name = country_name
        self.country_name = country_name

        self.scholarship_name = []
        self.scholarship_eligibility = []
        self.scholarship_amount = []
        self.scholarship_type = []
        self.scholarship_study_level = []
        self.no_of_scholarships = []

    # create our own method city_wise------
    def city(self):
        
        try:
            for i in range(1, 30):
            #------getting the URL request----
                user_agents_list = [
                'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                ]
                if(i==1):
                    response = requests.get(f'https://collegedunia.com/scholarship?gender={self.country_name}', headers={'User-Agent': random.choice(user_agents_list)})
                else:
                    response = requests.get(f'https://collegedunia.com/scholarship/page-{str(i)}?gender={self.country_name}', headers={'User-Agent': random.choice(user_agents_list)})

                response.raise_for_status()

                #---extracting whole data of URL in HTML format---
                data = BeautifulSoup(response.text, 'lxml')

                try:
                    #---write code here---
                    cards = data.find('div', class_="jsx-4142307919 jsx-3247734209 row").find_all('div', class_="jsx-2004262814 col-4 scholarship-card mb-4")
                    
                    for card in cards:
                            
                        try:
                            title = card.find('h2', class_="jsx-2004262814 m-0 scholar-card-heading p-3 text-truncate").text
                            self.scholarship_name.append(title)
                            
                            info = card.find('ul').find_all('li', class_="jsx-2004262814 pb-3 text-lg")
                            scholar_info = []
                            for l in info:
                                scholar_info.append(l.span.text)
                                
                            self.scholarship_eligibility.append(scholar_info[0])
                            self.scholarship_amount.append(scholar_info[1])
                            self.scholarship_type.append(scholar_info[2])
                            self.scholarship_study_level.append(scholar_info[3])
                            self.no_of_scholarships.append(scholar_info[4])           
                            

                        except Exception as e:
                            print(e)
                            
                except Exception as e:
                    print(e)


        except Exception as e:
            print(e)