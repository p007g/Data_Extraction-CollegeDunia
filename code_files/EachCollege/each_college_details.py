import bs


college_name = []
college_logo = []
upper_section_details = []
college_rating = []
college_summary = []
college_fees_eligibility = []
courses_details = []

try:

    # Upper Section--
    def getCollegeDetails(c_link):
        
        soup = bs.Soup(c_link)
        
        # college title--------
        clg_title = soup.find('h1', id="collegePageTitle").text.split(':')[0]
        college_name.append(clg_title)
        
        
        # college logo--------
        logo = soup.find('a', class_="jsx-201813991 logo bg-white")
        if logo is not None:
            url = logo.find('img').get('src')
            college_logo.append(url)
        else:
            college_logo.append("")
        
        
        # college info--------
        info = soup.find('div', class_="jsx-201813991 extra-info mr-8").find_all('span')

        empty = {"Place": '', "Approval": '', "Establishment": '', "University Type": ''}
        
        for i in info:
        
            if i.find('span', class_="jsx-201813991 icon icon-white pin-svg college-header-svg-list"):
                empty["Place"] = i.text.strip()
            elif i.find('span', class_="jsx-201813991 icon ribbon-svg college-header-svg-list icon-white"):
                empty["Approval"] = i.text.strip()
            elif i.find('span', class_="jsx-201813991 icon college-header-svg-list paper-svg icon-white"):
                empty["Establishment"] = i.text.strip()
            elif i.find('span', class_="jsx-201813991 icon star-svg college-header-svg-list icon-white"):
                empty["University Type"] = i.text.strip()
            
        l = empty
        upper_section_details.append(l)
        # college_place.append(l[0])
        # college_approval.append(l[1])
        # college_establishment.append(l[2])
        # college_universityType.append(l[3])
            
            
        # Rating----------
        rating = soup.find('span', class_="jsx-201813991 rating-val font-weight-bold d-inline-block")
        if rating is not None:
            college_rating.append(float(rating.text))
        else:
            college_rating.append("")
        
        
        # College details------
        college_highlights = soup.find('div', class_="cdcms_college_highlights")
        if college_highlights is not None:
            college_summary.append(college_highlights.p.text)
        else:
            college_summary.append("")
        
        
    # College fees and eligibility-----
    # def getfees(f_link):
    
    #     soup = bs.Soup(f_link)
    
        cfe = soup.find('section', class_="jsx-2589112289 fees-info table-data bg-white reserve-table-height p-5 rounded-xl college-shadow")
        
        if cfe is not None:
            courses = cfe.find('tbody', class_="jsx-2589112289 font-weight-normal").find_all('tr')
            
            all_courses = []
            for course in courses:
                # all_courses = []
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
                
                all_courses.append(crs)
        
        
            college_fees_eligibility.append(all_courses)
        else:
            college_fees_eligibility.append("--------------")
            
            
        
        # courses offered by colleges -----
        
        course_cards = soup.find('div', class_="jsx-2596245605 course-card-list").find_all('div', class_="jsx-819542916 course-body page_center_body_listing bg-white my-4 mx-5")
        
        college_courses = []
        for course_card in course_cards:
            each_course_details = {}
            
            # 1st row--
            course_name = course_card.find('h3', class_="jsx-819542916 text-title text-lg font-weight-bold mb-0 pr-5")
            if course_name is not None:
                each_course_details['CN'] = course_name.text.strip()
            else:
                each_course_details['CN'] = ""
            
            course_year = course_card.find('span', class_="jsx-819542916 year d-flex font-weight-medium text-sm mr-2")
            if course_year is not None:
                each_course_details['CY'] = course_year.text.strip()
            else:
                each_course_details['CY'] = ""
                

            
            course_degree = course_card.find('span', class_="jsx-819542916 degree d-flex font-weight-medium text-sm mr-2")
            if course_degree is not None:
                each_course_details['CD'] = course_degree.text.strip()
            else:
                each_course_details['CD'] = ""
            
            course_grad = course_card.find('span', class_="jsx-819542916 graduation d-flex font-weight-medium text-sm mr-2 text-silver")
            if course_grad is not None:
                each_course_details['CG'] = course_grad.text.strip()
            else:
                each_course_details['CG'] = ""
            
            
            course_time = course_card.find('span', class_="jsx-819542916 type d-flex font-weight-medium text-sm mr-2 text-college-link")
            if course_time is not None:
                each_course_details['CT'] = course_time.text.strip()
            else:
                each_course_details['CT'] = ""
            
            # 2nd row---
            
            course_rating = course_card.find('p', class_="jsx-819542916 m-0 text-primary font-weight-medium text-base")
            if course_rating is not None:
                each_course_details['CR'] = course_rating.text.split('/')[0]
            else:
                each_course_details['CR'] = ""
                
                
            # crated = course_card.p.find('span', class_="text-title")
            # each_cd['CRText'] = crated.text.strip()
            
            exam_accept = course_card.find('p', class_="jsx-819542916 mb-2")
            if exam_accept is not None:
                each_course_details['EA'] = exam_accept.find('a', class_="jsx-819542916 font-weight-medium hover-underline").text.strip()
            else:
                each_course_details['EA'] = "-"
                
            
            application_date = course_card.find('div', class_="jsx-819542916 course-details").find('span', class_="jsx-819542916 course-details-item-data text-title")
            if application_date is not None:
                each_course_details['AD'] = application_date.text.strip()
            else:
                each_course_details['AD'] = "-"
            
            
            application_fees = course_card.find('div', class_="jsx-819542916 ml-auto fees text-silver text-right font-weight-medium text-md")
            if application_fees is not None:
                each_course_details['AF'] = application_fees.text.strip()
            else:
                each_course_details['AF'] = ""
                
            college_courses.append(each_course_details)        
        
        
        courses_details.append(college_courses)
        

        
except Exception as e:
    print(e)
