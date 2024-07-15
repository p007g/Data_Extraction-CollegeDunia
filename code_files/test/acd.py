import beautiful_soup
    

#inside link
def getAbroadDetails(c_link):
    
    soup = beautiful_soup.Soup(c_link)
    
# College Upper---
   
    # college title--------
    # clg_title = soup.find('h1', class_="jsx-1056176865 text-white font-weight-bold mt-0 mb-1 text-lg").text
    # print(clg_title)
    
    
    # college logo--------
    logo = soup.find('a', class_="jsx-1056176865 college-logo bg-white")
    if logo is not None:
        url = logo.find('img').get('src')
        print(url)
    else:
        print("")
        
    
    # # college info--------
    # inf = soup.find('div', class_="jsx-1056176865 extra-info mt-2 d-flex")
    
    # if inf is not None:
        
    #     info = inf.find_all('div', class_="jsx-1056176865 info-wrap text-white font-weight-medium text-uppercase text-sm d-flex")
    
    #     tab = {}
    
    #     for i in info:
    #         try:
    #             condition = i.find('span', class_="jsx-1056176865 info-text text-capitalize")
    #             if condition is not None:
    #                 cond = condition.text
        
    #             statement = i.find('span', class_="jsx-1056176865 d-block text-md text-capitalize")
    #             if statement is not None:
    #                 stat = statement.text.strip()
            
                
    #             if cond == 'Location':
    #                 tab['Location'] = stat
                    
    #             if cond == 'School type':
    #                 tab['School type'] = stat
                
    #             if cond == 'established year':
    #                 tab['Established Year'] = stat
            
    #         except:
    #             print("")
                
                
    #     if not tab:
    #         print("---")
    #     else:
    #         print(tab)
    
    # else:
    #     print("=========")
        
        
    
    # Rating----------
    rating = soup.find('span', class_="jsx-1056176865 rating-val font-weight-bold d-inline-block")
    if rating is not None:
        print(float(rating.text.split('/')[0]))
    else:
        print("--")
    
    
    # # College details------
    # college_highlights = soup.find('div', class_="cdcms_section1")
    
    # if college_highlights is not None:
    #     para = college_highlights.find('p')
        
        
    #     if para is not None:
    #         print_para = para.text
    #         p_tag = college_highlights.find_all('p')
            
    #         # Check if there are at least two 'p' tags
    #         if print_para == "":
    #             # Get the text from the second 'p' tag
    #             print_para = p_tag[1].text  # Index 1 corresponds to the second element
            
       
    #         print(print_para)
            
    # else:
    #     print("No Info")
    
 
# College fees and eligibility-----

    '''
    table = soup.find('table', id = "tableData")
    
    if table is not None:
        
        body = table.find('tbody')
        
        if body is not None:
            blocks = body.find_all('tr', class_="jsx-1904507593 text-lg font-weight-medium")
            
            for block in blocks:
                fees_score = {}
                
                # program---
                program = block.find('td', class_="jsx-1904507593 col-program")
                type = program.span.a.text.strip()
                duration = program.find('div', class_="jsx-1904507593 duration tag d-inline-block badge-blue rounded font-weight-medium text-md text-capitalize").text.strip()
                
                fees_score['Program Type'] = type + " (" + duration + ")"
                
                
                # dates---
                dates = block.find('td', class_="jsx-1904507593 col-application-deadline")
                divs = dates.div.find_all('div', class_="jsx-1904507593 d-flex text-title rounded")
                
                date = ""
                for i in range(0, len(divs)):
                    
                    date = date + divs[i].find('span', class_="jsx-1904507593 text-capitalize").text.strip() + "\n"
                    
                    
                fees_score['Important Dates'] = date.rstrip("\n")
                
                
                # fees---
                fees = block.find('td', class_="jsx-1904507593 col-fees")
                
                fees_score['Fees'] = fees.span.text.strip()
                
                
                
                # exam score---
                sc = block.find('td', class_="jsx-1904507593 col-score")
                lt = sc.find('ul')
                
                if lt is not None:
                
                    list = lt.find_all('li', class_="jsx-1904507593 exam-score text-base text-nowrap")
                    
                    exam_score = ""
                    for i in range(0, len(list)):
                        
                        exam_name = list[i].find('span', class_="jsx-1904507593 text-gray").text.strip()
                        score = float(list[i].find('span', class_="jsx-1904507593 text-title font-weight-medium").text.strip())
                        
                        exam_score += f'{exam_name} {score}, '
                        
                        
                    fees_score['Exams Score'] = exam_score.rstrip(", ")
                
                else:
                    fees_score["Exams Score"] = None
            
            
                print(fees_score)
        
        else:
            print("!!!!!!!!!")
    else:
        print("::::::::::::::")
    '''            
            
        

# Courses Offered----


    cr_cards = soup.find('div', class_="jsx-3247734209 jsx-1647728581 top-clicked-card bg-white")
    # print(cr_cards)

    if cr_cards is not None:
        
        course_cards = cr_cards.find_all('div', class_="jsx-2492516079 jsx-2133140133 card-head d-flex justify-content-between px-3")
    
        for course_card in course_cards:
            each_course_details = {}

        
            # 1st row--
            course_name = course_card.find('h2', class_="jsx-2492516079 jsx-2133140133 card-heading m-0 h1 font-weight-bold text-lg pointer")
            if course_name is not None:
                each_course_details['Course Name'] = course_name.a.text.strip()
                # print(course_name.a.text.strip())
            # else:
            #     each_course_details['Course Name'] = ""
            
            
            course_year = course_card.find('div', class_="jsx-2492516079 jsx-2133140133 text-sm text-success d-flex align-items-center font-weight-medium")
            if course_year is not None:
                each_course_details['Course Duration'] = course_year.text.strip()
                # print(course_year.text.strip())
            # else:
            #     each_course_details['CY'] = ""
            
            # i=0
            # cdcs = course_card.find_all('span', class_="jsx-819542916 degree d-flex font-weight-medium text-sm mr-2")
            
            # for cdc in cdcs:
            #     i+=1
                
            #     if cdc.find('span', class_="jsx-819542916 mr-1 icon book-svg course-info-svg-list"):
            #         each_cd['CD'] = cdc.text.strip()
            #     if cdc.find('span', class_="jsx-819542916 mr-1 icon campus-svg course-info-svg-list"):
            #         each_cd['CC'] = cdc.text.strip()

            
            course_degree = course_card.find('div', class_="jsx-2492516079 jsx-2133140133 text-sm red-feature d-flex align-items-center font-weight-medium")
            if course_degree is not None:
                each_course_details['Course Degree'] = course_degree.text.strip()
                # print(course_degree.text.strip())
            # else:
            #     each_course_details['CD'] = ""
            
            course_grad = course_card.find('div', class_="jsx-2492516079 jsx-2133140133 text-sm silver-feature d-flex align-items-center font-weight-medium")
            if course_grad is not None:
                each_course_details['Course Language'] = course_grad.text.strip()
                # print(course_grad.text.strip())
            # else:
            #     each_course_details['CG'] = ""
            
            
            course_time = course_card.find('span', class_="jsx-2492516079 jsx-2133140133 text-capitalize")
            if course_time is not None:
                each_course_details['Course Time'] = course_time.text.strip()
                # print(course_time.text.strip())
            # else:
            #     each_course_details['CT'] = ""
            
            
            course_fees = course_card.find('span', class_="jsx-2492516079 jsx-2133140133 fees font-weight-bold text-lg mb-1")
            if course_fees is not None:
                each_course_details['Course Fees'] = course_fees.text.strip()
            
            
            
            # 2nd row---
            
            # course_rating = course_card.find('span', class_="jsx-4021726889 jsx-2133140133 font-weight-medium text-title")
            # if course_rating is not None:
            #     each_course_details['Course Rated'] = course_rating.text.split()
            # else:
            #     each_course_details['CR'] = ""
                
                
            # course_review = course_card.find('p', class_="jsx-819542916 m-0 text-primary font-weight-medium text-base").find('a', class_="jsx-819542916 text-base text-college-link")
            # if course_review is not None:
            #     each_course_details['review'] = course_review.text.strip()
                
                
            # crated = course_card.p.find('span', class_="text-title")
            # each_cd['CRText'] = crated.text.strip()
            
            # exam_accept = course_card.find('div', class_="jsx-4021726889 jsx-2133140133 card-info px-0 d-flex justify-content-between align-items-center")
            # if exam_accept is not None:
            #     each_course_details['EA'] = exam_accept.find('a', class_="jsx-819542916 font-weight-medium hover-underline").text.strip()
            # # else:
            # #     each_course_details['EA'] = "-"
                
            
            # app_date = course_card.find('div', class_="jsx-4021726889 jsx-2133140133 card-info mt-1 px-0 d-flex justify-content-between align-items-center font-weight-medium text-base")
            # if app_date is not None:
            #     application_date = app_date.find('span', class_="jsx-4021726889 jsx-2133140133 text-title")
            #     each_course_details['Application Date'] = application_date.text.strip()
            #     print(application_date.text.strip())
            # # else:
            # #     each_course_details['AD'] = "-"
            
            
            # application_fees = course_card.find('span', class_="jsx-4021726889 jsx-2133140133 fees font-weight-bold text-lg mb-1")
            # if application_fees is not None:
            #     each_course_details['Application Fees'] = application_fees.text.strip()
            #     print(application_fees.text.strip())
            # # else:
            # #     each_course_details['AF'] = ""
                
                
            print(each_course_details)
    
    else:
        print("")



# -------------------Main Function------------
# getAbroadDetails("https://collegedunia.com/uk/university/865-university-of-oxford-oxford")


# getfees("https://collegedunia.com/university/25881-iit-madras-indian-institute-of-technology-iitm-chennai")
# getCourses("https://collegedunia.com/college/18041-imt-institute-of-management-technology-ghaziabad")
# getFaculty("https://collegedunia.com/college/18041-imt-institute-of-management-technology-ghaziabad/faculty")