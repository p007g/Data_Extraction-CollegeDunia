import bs


institute_name = []
institute_logo = []
institute_city = []
institute_rating = []
# institute_summary = []
institute_type = []
# courses_details = []
Courses_Name = []
Courses_Fees = []
Courses_Time = []
Program_Type = []

try:

    # Upper Section--
    def getInstituteDetails(c_link):
        
        soup = bs.Soup(c_link)
        
        # institute title--------
        name = soup.find('h1', class_="jsx-3706751501 text-white font-weight-bolder mt-0 mb-1 text-lg").text
        institute_name.append(name)
        
        
        # institute logo--------
        logo = soup.find('a', class_="jsx-3706751501 college-logo bg-white p-1")
        if logo is not None:
            url = logo.find('img').get('data-src')
            institute_logo.append(url)
        else:
            institute_logo.append("")
            
            
        # institute location--
        loc = soup.find('div', class_="jsx-3706751501 extra-info").find('span', class_="jsx-3706751501 text-white text-uppercase font-weight-bold text-sm mr-3")
        if loc is not None:
            institute_city.append(loc.text.split(',')[0].strip())
            
        # Rating----------
        rating = soup.find('span', class_="jsx-3706751501 rating-val font-weight-bolder d-inline-block")
        if rating is not None:
            institute_rating.append(float(rating.text.split('/')[0]))
            
            
            
        # Institute details------
        content = soup.find('div', class_="jsx-1484856324 jsx-2394709119 article-body content-side college-content-section")
        
        if content is not None:
            
            # p1 = content.find('p')
            
            # if p1 is not None:
                
            #     para = p1.text
            
            #     p_tag = content.find_all('p')
                
            #     # Check if there are at least two 'p' tags
            #     if para == "":
            #         # Get the text from the second 'p' tag
            #         para = p_tag[1].text  # Index 1 corresponds to the second element
                
                
            #     institute_summary.append(para)
                
            # else:
            #     institute_summary.append("")
        
        
            # # table---
            inf = content.find('table', class_="table table-bordered table-striped")
            
            if inf is not None:
                info = inf.tbody.find('tr')
                
                # tab = {}
                
                # for i in range(0, len(info)):
                
                cond = info.find_all('td')[0].text
                stat = info.find_all('td')[1].text.strip()
                
                if cond == 'Institute Type':
                    institute_type.append(stat)
                        
                    # if cond == 'Established in':
                    #     tab['Established in'] = stat
                    
                    # if cond == 'Established':
                    #     tab['Established'] = stat
                        
                    # if cond == 'Official Website':
                    #     tab['Official Website'] = stat
                        
                    # if cond == 'Email':
                    #     tab['Email'] = stat
                        
                    # if cond == 'Study Material':
                    #     tab['Study Material'] = stat
                
                # if not InstituteType:
                #     institute_type.append(None)
                # else:
                #     institute_type.append(InstituteType)
                
            else:
                institute_type.append(None)
        
        
        
        # courses offered by Institutes -----
        
        cr_cards = soup.find('div', class_="jsx-1280987842 courses")
        
        if cr_cards is not None:
            
            course_cards = cr_cards.find_all('div', class_="jsx-1096428961 program-card mt-4 bg-white")
            institute_courses = []
            institute_courses_name = []
            institute_courses_fees = []
            institute_courses_type = []
            institute_courses_time = []
            
            for course_card in course_cards:
                each_course_details = {}
                
                # 1st row--
                course_name = course_card.find('h3', class_="jsx-1096428961 text-secondary h2 mb-0")
                if course_name is not None:
                    cn = course_name.a.text.strip()
                    if ':' in cn:
                        each_course_details['Course Name'] = course_name.a.text.split(':')[1].strip()
                    else:
                        each_course_details['Course Name'] = course_name.a.text.strip()
                    
                    
                course_fees = course_card.find('div', class_="jsx-1096428961 fees")
                if course_fees is not None:
                    each_course_details['Course Fees'] = course_fees.span.text.strip()
                    
                    
                # 2nd row--
                course_time = course_card.find('span', class_="jsx-1096428961 year align-items-center font-weight-bold text-sm mr-6")
                if course_time is not None:
                    each_course_details['Course Time'] = course_time.text.strip()
                
                
                course_type = course_card.find('span', class_="jsx-1096428961 d-block sub-head text-silver")
                if course_type is not None:
                    each_course_details['Program Type'] = course_type.text.strip()

                
                    
                # institute_courses.append(each_course_details) 
                institute_courses_name.append(each_course_details['Course Name'])
                institute_courses_fees.append(each_course_details['Course Fees'])
                institute_courses_time.append(each_course_details['Course Time'])
                institute_courses_type.append(each_course_details['Program Type'])
            
            
            # courses_details.append(institute_courses)
            Courses_Name.append(institute_courses_name)
            Courses_Fees.append(institute_courses_fees)
            Courses_Time.append(institute_courses_time)
            Program_Type.append(institute_courses_type)
            
        # else:
        #     courses_details.append(None)
        

        
except Exception as e:
    print(e)
