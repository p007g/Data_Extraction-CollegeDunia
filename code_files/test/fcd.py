import requests
from bs4 import BeautifulSoup
import random

#inside link
def getCourseDetails(c_link):
    
    #------getting the URL request----
    user_agents_list = [
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]

    response = requests.get(c_link, headers={'User-Agent': random.choice(user_agents_list)})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')

    details = soup.find('div', class_="cdcms_courses")
    
    # fulld = ""
    # for d in details:
    #     if "1.1" in d.text:
    #         break
    #     else:
    #         fulld = fulld + "\n" + d.text.strip()
        
    # return fulld
    
    if details is not None:
        return details.p.text
    else:
        return "#############"
        
    
# cse_dtl = getCourseDetails("https://collegedunia.com/courses/bachelor-of-science-bsc-mathematics")
# print(cse_dtl)