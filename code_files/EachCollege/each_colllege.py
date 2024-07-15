from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import timeit
import time
import csv
from selenium import webdriver
# import each_college_details as ecd
import clg_details as ecd

# start timer
start_time = timeit.default_timer()


# Set up the Selenium WebDriver
path_to_chromedriver = "C:\Program Files (x86)\chromedriver.exe"

cService = webdriver.ChromeService(executable_path=path_to_chromedriver)
driver = webdriver.Chrome(service = cService)


# Open the web page
# indian_states = ["andhra-pradesh--", "arunachal-pradesh--", "assam--", "andaman-and-nicobar-islands--", "bihar--", "chandigarh--", "chhattisgarh--", 
#                  "daman-and-diu--", "delhi-ncr--", "goa--", "gujarat--", "haryana"--, "himachal-pradesh--", 
#                  "jammu-and-kashmir--", "jharkhand--", "karnataka--", "kerala--", "madhya-pradesh--", "maharashtra--", "manipur--", 
#                  "meghalaya--", "mizoram--", "nagaland--", "odisha--", "punjab--", "puducherry--", "rajasthan--", "sikkim--", "tamil-nadu", 
#                  "telangana--", "tripura--", "uttar-pradesh", "uttarakhand--",
#                  "west-bengal--"]

# states =["assam", "andaman-and-nicobar-islands"]


# for state in states:
state = "punjab"


driver.get(f'https://collegedunia.com/{state}-colleges')


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
        time.sleep(5)
        
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
    blocks = data.find('div', class_="jsx-4033392124 jsx-1933831621 table-view-wrapper india real position-relative w-100").find_all('div', class_="jsx-4033392124 jsx-1933831621 table-wrapper")
    
    for block in blocks:
            
        try:
            ccs = block.find('tbody', class_="jsx-4033392124 jsx-1933831621").find_all('tr')
            
            for cc in ccs:
                link = cc.find('a', class_="jsx-3749532717 clg-logo d-block mr-2")
                
                if link is not None:
                    college_link = link.get('href')
                    f_college_link = f'https://collegedunia.com{college_link}'
                    
                    # finder course details @link---
                    ecd.getCollegeDetails(f_college_link)
                    
                    
                                        
                else:
                    continue
                
        except:
            print("")
            
except Exception as e:
    print(e)
    
    
# Close the browser
driver.quit()
        

try:        
    fields = {
        "College_Name":ecd.college_name,
        # "College_Logo":ecd.college_logo,
        # "Upper_Section_Details":ecd.upper_section_details,
        # "College_Rating":ecd.college_rating,
        # "College_Summary":ecd.college_summary,
        # "Fees_and_Eligibility":ecd.college_fees_eligibility,
        # "Courses_Details":ecd.courses_details
        "Course_Name":ecd.Courses_Name,
        "Course_Year":ecd.Courses_Year,
        "Course_Time":ecd.Courses_Time
        }

    df = pd.DataFrame.from_dict(fields, orient='index')
    df = df.transpose()
    
    
        
    chunk_size = 300  # Adjust the number of rows per file as needed
    num_chunks = len(df) // chunk_size + (1 if len(df) % chunk_size else 0)

    for i in range(num_chunks):
        new_df = df[i*chunk_size:(i+1)*chunk_size]
        
        # csv_file_path = f'extracted_files\state_wise_college_course_details\{state}_data_{i+1}.csv'
        # new_df.to_csv(csv_file_path, index=False)
        
        json_file_path = f'extracted_files\state_wise_college_course_details_2\{state}_data_{i+1}.json'
        new_df.to_json(json_file_path, orient='records')
        
    # json_file_path = f'extracted_files\state_colleges\{state}_data.json'
    # df.to_json(json_file_path, orient='records')
        
        
    
except Exception as e:
    print(e)

# print(len(ecd.college_name), len(ecd.college_place), len(ecd.college_approval), len(ecd.college_establishment), len(ecd.college_universityType), len(ecd.college_rating), len(ecd.college_detail))
print(df)


# Save to files------
# excel_file = 'extracted_files\each_college\sample_data_05.csv'
# df.to_csv(excel_file, index=False)


# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")