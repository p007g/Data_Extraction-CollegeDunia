from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import timeit
import time
from selenium import webdriver
import ecd


# start timer
start_time = timeit.default_timer()

# Set up the Selenium WebDriver
path_to_chromedriver = "C:\Program Files (x86)\chromedriver.exe"

cService = webdriver.ChromeService(executable_path=path_to_chromedriver)
driver = webdriver.Chrome(service = cService)

# # Open the web page
# driver.get('https://collegedunia.com/goa-colleges')


# # Wait for the dynamic content to load
# time.sleep(5)


# Open the web page
state = 'sikkim-colleges'
driver.get(f'https://collegedunia.com/{state}')


# Wait for the dynamic content to load
time.sleep(5)
print("loading...")


# Execute JavaScript to scroll to the bottom of the page
try:
    previous_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for new content to load
        time.sleep(4)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == previous_height:
            break
        previous_height = new_height
        
except Exception as e:
    print(e)



#---extracting whole data of URL in HTML format---
data = BeautifulSoup(driver.page_source, 'lxml')

try:
    #---write code here---
    blocks = data.find('div', class_="jsx-2796823646 jsx-1933831621 table-view-wrapper india real position-relative w-100").find_all('div', class_="jsx-2796823646 jsx-1933831621 table-wrapper")
    
    for block in blocks:
            
        try:
            ccs = block.find('tbody', class_="jsx-2796823646 jsx-1933831621").find_all('tr')
            
            for cc in ccs:
                link = cc.find('a', class_="jsx-1948362374 clg-logo d-block mr-2")
                # print(link)
                
                if link is not None:
                    college_link = link.get('href')
                    f_college_link = f'https://collegedunia.com{college_link}'
                    # print(f_college_link)
                    
                    # finder course details @link---
                    ecd.getCollegeDetails(f_college_link)
                    
                    # course fees and eligibility---
                    # ecd.getfees(f_college_link)
                    
                    # courses offered--
                    ecd.getCourses(f_college_link)
                    
                    print("-------------------------------------------------------------------------------")
                    
                else:
                    continue
                
                print("")

        except:
            print("")
            
except Exception as e:
    print(e)
    

# Close the browser
driver.quit()
        

# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")