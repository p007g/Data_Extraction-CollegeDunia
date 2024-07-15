import beautiful_soup


def print_dict_without_quotes(d):
    items = []  # List to store formatted string versions of dictionary items
    for key, value in d.items():
        # Convert both keys and values to strings and format without quotes
        item = f"{str(key)}: {str(value)}"
        items.append(item)
    formatted_dict = "{" + ", ".join(items) + "}"
    return formatted_dict
    
    

#inside link
def getCollegeDetails(c_link):
    
    soup = beautiful_soup.Soup(c_link)
    
    
    # college title--------
    clg_title = soup.find('h1', id="collegePageTitle").text.split(':')[0]
    print(clg_title)
    
    '''
    # college logo--------
    logo = soup.find('a', class_="jsx-201813991 logo bg-white")
    if logo is not None:
        url = logo.find('img').get('src')
        print(url)
    else:
        print("")
        
    
    # college info--------
    info = soup.find('div', class_="jsx-201813991 extra-info mr-8").find_all('span')
    
    empty = {'P': '', "A": '', "E": '', "U": ''}
    
    for i in info:
        
        if i.find('span', class_="jsx-201813991 icon icon-white pin-svg college-header-svg-list"):
            empty["P"] = i.text.strip()
        elif i.find('span', class_="jsx-201813991 icon ribbon-svg college-header-svg-list icon-white"):
            empty["A"] = i.text.strip()
        elif i.find('span', class_="jsx-201813991 icon college-header-svg-list paper-svg icon-white"):
            empty["E"] = i.text.strip()
        elif i.find('span', class_="jsx-201813991 icon star-svg college-header-svg-list icon-white"):
            empty["U"] = i.text.strip()
            
    r = empty
    print(print_dict_without_quotes(r))
        
    # Rating----------
    rating = soup.find('span', class_="jsx-201813991 rating-val font-weight-bold d-inline-block")
    if rating is not None:
        print(float(rating.text))
    else:
        print("--")
    
    
    # College details------
    college_highlights = soup.find('div', class_="cdcms_college_highlights")
    if college_highlights is not None:
        print(college_highlights.p.text)
    else:
        print("No Info")
    
    
# College fees and eligibility-----
def getfees(f_link):
    
    soup = beautiful_soup.Soup(f_link)
    
    cfe = soup.find('section', class_="jsx-2589112289 fees-info table-data bg-white reserve-table-height p-5 rounded-xl college-shadow")
    
    courses = cfe.find('tbody', class_="jsx-2589112289 font-weight-normal").find_all('tr')
    
    for course in courses:
        crs = {}
        all_td = course.find_all('td')
        
        cons = 0
        for td in all_td:
            cons+=1
            
            if cons==1:
                crs['Course'] = td.text
            elif cons==2:
                crs['Fees'] = td.text
            elif cons==3:
                crs['Eligibility'] = td.text
            else:
                break
        
        # c_name = course.find('td', class_="jsx-2589112289 font-weight-medium").a.text.strip()
        # crs['Course'] = c_name
        
        # c_fees = course.find_next('td', class_="jsx-2589112289").text.strip()
        # crs['Fees'] = c_fees
        
        # # c_eligibility = course.find('td', class_="jsx-2589112289").td.text.strip()
        # # crs.append(c_eligibility)
        
        print(crs)
        '''
        
        
def getCourses(co_link):
    
    soup = beautiful_soup.Soup(co_link)
    
    course_cards = soup.find('section').find_all('div', class_="jsx-1671751200 course-card border border-gray-5 rounded-8 p-4 mt-4")
    # print(course_cards)
    
    for course_card in course_cards:
        each_course_details = {'CN': "", 'CY': "", 'CT': ""}
        
        # 1st row--
        course_name = course_card.find('div', class_="jsx-1671751200 course-detail d-flex justify-content-between")
        if course_name is not None:
            each_course_details['CN'] = course_name.a.text.strip()

        
        course_year = course_card.find('div', class_="jsx-1671751200 fs-14 font-weight-normal text-dark-grey d-flex")
        if course_year is not None:
            
            sp = course_year.find_all('span', class_="jsx-1671751200 course-separater pl-3 ml-2 position-relative")
            for s in sp:
                txt = s.text.strip()
                # print(txt)
                if "years" and "year" in txt.lower():
                    each_course_details['CY'] = txt
                    
                elif "time" in txt.lower():
                    each_course_details['CT'] = txt

        
    #     course_degree = course_card.find('span', class_="jsx-819542916 degree d-flex font-weight-medium text-sm mr-2")
    #     if course_degree is not None:
    #         each_course_details['CD'] = course_degree.text.strip()
    #     # else:
    #     #     each_course_details['CD'] = ""
        
    #     course_grad = course_card.find('span', class_="jsx-819542916 graduation d-flex font-weight-medium text-sm mr-2 text-silver")
    #     if course_grad is not None:
    #         each_course_details['CG'] = course_grad.text.strip()
    #     # else:
    #     #     each_course_details['CG'] = ""
        
        
    #     course_time = course_card.find('span', class_="jsx-819542916 type d-flex font-weight-medium text-sm mr-2 text-college-link")
    #     if course_time is not None:
    #         each_course_details['CT'] = course_time.text.strip()
    #     # else:
    #     #     each_course_details['CT'] = ""
        print(each_course_details)
        
'''
        # 2nd row---
        
        course_rating = course_card.find('p', class_="jsx-819542916 m-0 text-primary font-weight-medium text-base")
        if course_rating is not None:
            each_course_details['CR'] = course_rating.text.split('/')[0]
        # else:
        #     each_course_details['CR'] = ""
            
            
        course_review = course_card.find('p', class_="jsx-819542916 m-0 text-primary font-weight-medium text-base").find('a', class_="jsx-819542916 text-base text-college-link")
        if course_review is not None:
            each_course_details['review'] = course_review.text.strip()
            
            
        # crated = course_card.p.find('span', class_="text-title")
        # each_cd['CRText'] = crated.text.strip()
        
        exam_accept = course_card.find('p', class_="jsx-819542916 mb-2")
        if exam_accept is not None:
            each_course_details['EA'] = exam_accept.find('a', class_="jsx-819542916 font-weight-medium hover-underline").text.strip()
        # else:
        #     each_course_details['EA'] = "-"
            
        
        application_date = course_card.find('div', class_="jsx-819542916 course-details").find('span', class_="jsx-819542916 course-details-item-data text-title")
        if application_date is not None:
            each_course_details['AD'] = application_date.text.strip()
        # else:
        #     each_course_details['AD'] = "-"
        
        
        application_fees = course_card.find('div', class_="jsx-819542916 ml-auto fees text-silver text-right font-weight-medium text-md")
        if application_fees is not None:
            each_course_details['AF'] = application_fees.text.strip()
        # else:
        #     each_course_details['AF'] = ""
            
        '''    
        # print(each_course_details)
        
'''
def getFaculty(faculty_link):
    
    soup = beautiful_soup.Soup(faculty_link)
    
    card = soup.find('div', class_="jsx-2968715513 detail card-body p-4")
    
    if card is not None:
        head = {}
        
        head_name = card.find('span', class_="jsx-2968715513 name text-capitalize font-weight-bold text-lg text-primary d-block mb-1")
        head_position = card.find('span', class_="jsx-2968715513 text-silver text-md font-weight-bold text-capitalize")
        
        if head_name is not None:
            head['Head Name'] = head_name.text
            
        if head_position is not None:
            head['Position'] = head_position.text
        
        print(head)
        
        other_faculties = soup.find('div', class_="jsx-2968715513 faculties pt-4").find_all('div', class_="jsx-2968715513 faculty-card d-flex align-items-start p-2")
        
        for f in other_faculties:
            
            f_details = {}
            
            f_name = f.find('h5', class_="jsx-2968715513 name text-success font-weight-bold text-capitalize mb-1")
            if f_name is not None:
                f_details['Name'] = f_name.text.strip()
            
            f_position = f.find('p', class_="jsx-2968715513 deprt text-primary font-weight-bold text-capitalize text-md mb-1")
            if f_position is not None:
                f_details['Position'] = f_position.text.strip()
            
            qual = f.find('span', class_="jsx-2968715513 text-silver")
            if qual is not None:
                f_details['Q'] = qual.text.strip()
            
            s_expertise = f.find('span', class_="jsx-2968715513 text-capitalize text-silver")
            if s_expertise is not None:
                f_details['SE'] = s_expertise.text.strip()
            
            email = f.find('p', class_="jsx-2968715513 email text-secondary font-weight-bold text-capitalize text-md mb-1 d-flex").find('span', class_="jsx-2968715513 text-silver text-lowercase")
            if email is not None:
                f_details['email'] = email.text.strip()
                    
                
            print(f_details)
            
    else:
        print("!!!!!!!!!!!!!!!!!!")
    '''


# -------------------Main Function------------
# getCollegeDetails("https://collegedunia.com/college/18041-imt-institute-of-management-technology-ghaziabad")
# getfees("https://collegedunia.com/university/25881-iit-madras-indian-institute-of-technology-iitm-chennai")
# getCourses("https://collegedunia.com/college/18041-imt-institute-of-management-technology-ghaziabad")
# getFaculty("https://collegedunia.com/college/18041-imt-institute-of-management-technology-ghaziabad/faculty")