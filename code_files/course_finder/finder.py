from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import timeit
import time
from selenium import webdriver
import finder_course_details

# start timer
start_time = timeit.default_timer()


course_name = []
course_duration = []
course_type = []
course_level = []
program_type = []
course_eligibility = []
entrance_exam = []
course_details = []
popular_job_roles = []
top_colleges = []


# Set up the Selenium WebDriver
path_to_chromedriver = "C:\Program Files (x86)\chromedriver.exe"

cService = webdriver.ChromeService(executable_path=path_to_chromedriver)
driver = webdriver.Chrome(service = cService)

# Open the web page
driver.get('https://collegedunia.com/course-finder')


# Wait for the dynamic content to load
time.sleep(400)


#---extracting whole data of URL in HTML format---
data = BeautifulSoup(driver.page_source, 'lxml')

try:
    #---write code here---
    courses = data.find('div', class_="jsx-694873018").find_all('div', class_="jsx-2903398554 course-card mb-4 p-4 border-4")
    
    for course in courses:
            
        try:
            
            #--------------------course name-------------------------
            cn = course.find('h3', class_="jsx-2903398554 text-xlg").text
            course_name.append(cn)
            
            
            #--------------------course infos-------------------------
            info = course.find('div', class_="jsx-2903398554 labels d-flex").find_all('span')
            course_info = []
            for s in info:
                course_info.append(s.text)
                
            course_duration.append(course_info[0])
            course_type.append(course_info[2].strip())
            course_level.append(course_info[4].strip())
            program_type.append(course_info[6].strip())
            
            
            #--------------------course eligibility-------------------------
            ce = course.find('span', class_="jsx-2903398554 pr-3 font-weight-semi")
            if ce is not None:
                course_eligibility.append(ce.text.split(':\xa0')[1])
            else:
                course_eligibility.append("")

            
            #--------------------entrance exam-------------------------
            ee = course.find('span', class_="jsx-2903398554 px-3 font-weight-semi")
            if ee is not None:
                entrance_exam.append(ee.a.text)
            else:
                entrance_exam.append("")
                
                
            #--------------------course details-------------------------
            try:
                cd = course.find('div', class_="jsx-2903398554 text-gray position-relative description").a.get('href')
                link = f"https://collegedunia.com{cd}"
                            
                # finder course details @link---
                crse_dtl = finder_course_details.getCourseDetails(link)
                
                course_details.append(crse_dtl)
            
            except:
                course_details.append("")
            
            
            #--------------------Job roles-------------------------
            pjrs = course.find('div', class_="jsx-2903398554 d-flex align-items-center").find_all('span')
            pjr = []
            for p in pjrs:
                pjr.append(p.text)
            
            popular_job_roles.append(", ".join(pjr[1:]))
            
            
            #--------------------top colleges-------------------------
            tclgs = course.find('div', class_="jsx-2903398554 d-flex colleges-data").find_all('a', class_="jsx-2903398554 text-link college-snippet d-flex align-items-center")
            tclg = []
            for tc in tclgs:
                tclg.append(tc.text)
                
            top_colleges.append("| ".join(tclg[:2]))
            

        except Exception as e:
            print(e)
            
except Exception as e:
    print(e)
    
    
# Close the browser
driver.quit()
        

try:        
    fields = {
        "Course":course_name,
        "Course Duration":course_duration, 
        "Course Type":course_type,
        "Course Level":course_level,
        "Program Type":program_type,
        "Course Eligibility":course_eligibility,
        "Entrance Exam":entrance_exam,
        "Course Details": course_details,
        "Popular Job Roles":popular_job_roles,
        "Top Colleges":top_colleges
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
excel_file = 'extracted_files\course_finder_updated.xlsx'
df.to_excel(excel_file)



# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")