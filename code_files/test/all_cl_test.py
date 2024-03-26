from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import timeit
import time
from selenium import webdriver


clg_name = []
logo_link = []


# start timer
start_time = timeit.default_timer()


# Set up the Selenium WebDriver
path_to_chromedriver = "C:\Program Files (x86)\chromedriver.exe"

cService = webdriver.ChromeService(executable_path=path_to_chromedriver)
driver = webdriver.Chrome(service = cService)

# Open the web page
driver.get('https://collegedunia.com/goa-colleges')


# Wait for the dynamic content to load
time.sleep(3)


#---extracting whole data of URL in HTML format---
data = BeautifulSoup(driver.page_source, 'lxml')

try:
    #---write code here---
    blocks = data.find('div', class_="jsx-2796823646 jsx-1933831621 table-view-wrapper india real position-relative w-100").find_all('div', class_="jsx-2796823646 jsx-1933831621 table-wrapper")
    
    for block in blocks:
            
        try:
            ccs = block.find('tbody', class_="jsx-2796823646 jsx-1933831621").find_all('tr')
            
            for cc in ccs:
                
                details = {}
                
                name = cc.find('a', class_="jsx-1948362374 college_name underline-on-hover")
                if name is not None:
                    details['Name'] = name.find('h3').text.split(',')[0]
                
                
                loc = cc.find('span', class_="jsx-1948362374 pr-1 location")
                if loc is not None:
                    details['Location'] = loc.text.strip()
                    
                if details:
                    print(details)
                    
                    
                # detail = {
                #     "Name": n,
                #     "Location": l
                # }
                
                # print(n)
                
                link = cc.find('a', class_="jsx-1948362374 clg-logo d-block mr-2")
                
                if link is not None:
                    # college_link = link.get('href')
                    logo_url = link.find('img').get('data-src')
                
                    print(logo_url)
                    
                    print("-------------------------------------------------------------------------------")
                                        
                # else:
                #     continue
                
        except:
            print("")
            
except Exception as e:
    print(e)
    
    
# Close the browser
driver.quit()
        
'''
try:        
    fields = {
        "College Name":ecd.college_name,
        "Place":ecd.college_place, 
        "Approval":ecd.college_approval,
        "Establishment":ecd.college_establishment,
        "University Type":ecd.college_universityType,
        "College Rating":ecd.college_rating,
        "College Summary":ecd.college_detail
        }

    df = pd.DataFrame.from_dict(fields, orient='index')
    df = df.transpose()
    # df.index = np.arange(1, len(df) + 1)
    # df["Sr-No"] = np.arange(1, len(df) + 1)
    # df = df.set_index('Sr-No')
    
    
    
    chunk_size = 600  # Adjust the number of rows per file as needed
    num_chunks = len(df) // chunk_size + (1 if len(df) % chunk_size else 0)

    for i in range(num_chunks):
        new_df = df[i*chunk_size:(i+1)*chunk_size]
        new_df.to_csv(f'extracted_files\each_college\college_data_{i+1}.csv', index=False)
        
    
except Exception as e:
    print(e)

print(len(ecd.college_name), len(ecd.college_place), len(ecd.college_approval), len(ecd.college_establishment), len(ecd.college_universityType), len(ecd.college_rating), len(ecd.college_detail))
print(new_df)


# Save to files------
# excel_file = 'extracted_files\each_college\sample_data_05.csv'
# df.to_csv(excel_file, index=False)
'''

# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")