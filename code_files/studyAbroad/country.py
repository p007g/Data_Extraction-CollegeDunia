import requests
from bs4 import BeautifulSoup
import random


class Abroad:
    
    university_country = []
    university_name = []
    university_place = []

    # class default method------
    def __init__(self, country_name):
        self.country_name = country_name


    # create our own method city_wise------
    def city(self):
        
        try:
            for i in range(1, 22):
            #------getting the URL request----
                user_agents_list = [
                'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                ]
                if(i==1):
                    response = requests.get(f'https://collegedunia.com/{self.country_name}-universities', headers={'User-Agent': random.choice(user_agents_list)})
                else:
                    response = requests.get(f'https://collegedunia.com/{self.country_name}-universities/page-'+str(i), headers={'User-Agent': random.choice(user_agents_list)})
                
                response.raise_for_status()
            

                #---extracting whole data of URL in HTML format---
                data = BeautifulSoup(response.text, 'html5lib')

                #---write code here---
                universities = data.find('tbody', class_="jsx-1597785535").find_all_next('tr', class_="jsx-3255989801 automate_client_img_snippet")

                
                for university in universities:        

                    university_info = university.find('span', class_="jsx-3255989801 flex-fill")

                    name = university_info.find('h3').text
                    Abroad.university_name.append(name)

                    place = university_info.find('span', class_="jsx-3255989801 text-gray text-md mr-2 text-capitalize").text
                    Abroad.university_place.append(place)

                    country = university_info.find('span', class_="jsx-3255989801 text-gray text-md mr-2 text-capitalize").text.split(',')[1]
                    Abroad.university_country.append(country)

                    # tuition_living = university.find('span', class_="jsx-3255989801 col-fees d-flex flex-column").text.split()


        except Exception as e:
            print(e)