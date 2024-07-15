import bs


institute_name = []
institute_logo = []
institute_location = []
institute_rating = []
institute_summary = []
institute_content = []
courses_details = []

try:

    # Upper Section--
    def getInstituteDetails(c_link):
        
        soup = bs.Soup(c_link)
        
        # institute title--------
        name = soup.find('h1', class_="jsx-2553403396 fs-24 font-weight-bold text-white").text
        institute_name.append(name)
        
        
        # institute logo--------
        logo = soup.find('a', class_="jsx-2553403396 institute-college-logo bg-white")
        if logo is not None:
            url = logo.find('img').get('data-src')
            institute_logo.append(url)
        else:
            institute_logo.append("")
            
            
        # institute location--
        loc = soup.find('div', class_="jsx-2553403396 extra-info mt-2 d-flex").find('span', class_="jsx-2553403396 fs-14 font-weight-normal text-white d-flex align-items-center")
        if loc is not None:
            institute_location.append(loc.text.split(',')[0].strip())
            
        # Rating----------
        rating = soup.find('div', class_="jsx-2553403396 fs-16 font-weight-semi marginr-2")
        if rating is not None:
            institute_rating.append(float(rating.text.split('/')[0]))
            
            
            
        # Institute details------
        content = soup.find('div', class_="jsx-1274291169 jsx-3815267175 article-body content-side content_box college-content-section wrap-body-small")
        
        if content is not None:
            
            p1 = content.find('p')
            
            if p1 is not None:
                
                para = p1.text
            
                p_tag = content.find_all('p')
                
                # Check if there are at least two 'p' tags
                if para == "":
                    # Get the text from the second 'p' tag
                    para = p_tag[1].text  # Index 1 corresponds to the second element
                    
                
                if "table of content" or "table of contents" in para:
                    institute_summary.append("")
                else:
                    institute_summary.append(para)
                
            else:
                institute_summary.append("")
        
        
            # # table---
            inf = content.find('table', class_="table table-bordered table-striped")
            
            if inf is not None:
                info = inf.tbody.find_all('tr')
                
                tab = {}
                
                for i in range(0, len(info)):
                    
                    cond = info[i].find_all('td')[0].text
                    stat = info[i].find_all('td')[1].text.strip()
                    
                    if cond == 'Institute Type':
                        tab['Institute Type'] = stat
                        
                    if cond == 'Established in':
                        tab['Established in'] = stat
                    
                    if cond == 'Established':
                        tab['Established'] = stat
                        
                    if cond == 'Official Website':
                        tab['Official Website'] = stat
                        
                    if cond == 'Email':
                        tab['Email'] = stat
                        
                    if cond == 'Study Material':
                        tab['Study Material'] = stat
                
                if not tab:
                    institute_content.append(None)
                else:
                    institute_content.append(tab)
                
            else:
                institute_content.append(None)
        
        
        
        # courses offered by Institutes -----
        
        cr_cards = soup.find('div', class_="jsx-1280987842 course-reserve-height")
        
        if cr_cards is not None:
            
            course_cards = cr_cards.find_all('div', class_="jsx-3128659336 course-card border border-gray-5 rounded-8 p-4 mt-4")
            institute_courses = []
            
            for course_card in course_cards:
                each_course_details = {}
                
                # 1st row--
                course_name = course_card.find('div', class_="jsx-3128659336 course-detail d-flex justify-content-between")
                if course_name is not None:
                    cn = course_name.a.text.strip()
                    if ':' in cn:
                        each_course_details['Course Name'] = course_name.a.text.split(':')[1].strip()
                    else:
                        each_course_details['Course Name'] = course_name.a.text.strip()
                    
                    
                course_fees = course_card.find('div', class_="jsx-3128659336 text-end ml-4 white-space-nowrap")
                if course_fees is not None:
                    each_course_details['Course Fees'] = course_fees.find('span', class_="jsx-3128659336 fs-18 font-weight-semi text-primary-green ml-1").text.strip()
                    
                    
                # 2nd row--
                course_time = course_card.find('span', class_="jsx-3128659336 position-relative")
                if course_time is not None:
                    each_course_details['Course Time'] = course_time.text.strip()
                
                
                course_type = course_card.find('span', class_="jsx-3128659336 course-separater pl-3 ml-2 position-relative")
                if course_type is not None:
                    each_course_details['Program Type'] = course_type.text.strip()

                
                    
                institute_courses.append(each_course_details)        
            
            
            courses_details.append(institute_courses)
            
        else:
            courses_details.append(None)
        

        
except Exception as e:
    print(e)
