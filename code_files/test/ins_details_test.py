import beautiful_soup

try:
    
    #inside link
    def getInstituteDetails(c_link):
        
        soup = beautiful_soup.Soup(c_link)
        
        
        # institute title--------
        institute_name = soup.find('h1', class_="jsx-2553403396 fs-24 font-weight-bold text-white").text
        print(institute_name)
        
        
        # institute logo--------
        logo = soup.find('a', class_="jsx-2553403396 institute-college-logo bg-white")
        if logo is not None:
            url = logo.find('img').get('data-src')
            print(url)

            
                    
        # institute location--
        loc = soup.find('div', class_="jsx-2553403396 extra-info mt-2 d-flex").find('span', class_="jsx-2553403396 fs-14 font-weight-normal text-white d-flex align-items-center")
        if loc is not None:
            print(loc.text.split(',')[0].strip())
            
            
        # Rating----------
        rating = soup.find('div', class_="jsx-2553403396 fs-16 font-weight-semi marginr-2")
        if rating is not None:
            print(float(rating.text.split('/')[0]))
            
            
            
        # Institute details------
        content = soup.find('div', class_="jsx-1274291169 jsx-3815267175 article-body content-side content_box college-content-section wrap-body-small")
        # print(content)
        if content is not None:
            
            p1 = content.find('p')
            
            if p1 is not None:
                
                para = p1.text
            
                p_tag = content.find_all('p')
                
                # Check if there are at least two 'p' tags
                if para == "":
                    # Get the text from the second 'p' tag
                    para = p_tag[1].text  # Index 1 corresponds to the second element
                
                
                print(para)
        
        
            # table---
            inf = content.find('table', class_="table table-bordered table-striped")
            
            if inf is not None:
                info = inf.tbody.find_all('tr')
                # print(info)
                
                tab = {}
                
                for i in range(0, len(info)):
                    
                    cond = info[i].find_all('td')[0].text
                    # print(cond)
                    stat = info[i].find_all('td')[1].text.strip()
                        
                    if cond == 'Institute Type':
                        tab['Institute Type'] = stat
                        
                    if cond == 'Established in':
                        tab['Established in'] = stat
                        
                    if cond == 'Official Website':
                        tab['Official Website'] = stat
                        
                    if cond == 'Email':
                        tab['Email'] = stat
                        
                    if cond == 'Study Material':
                        tab['Study Material'] = stat
                    
                print(tab)
        
        else:
            print("No Info") 
    
    # Courses----
        
        course_cards = soup.find('div', class_="jsx-1280987842 course-reserve-height").find_all('div', class_="jsx-3128659336 course-card border border-gray-5 rounded-8 p-4 mt-4")
        
        for course_card in course_cards:
            each_course_details = {}
            
            # 1st row--
            course_name = course_card.find('div', class_="jsx-3128659336 course-detail d-flex justify-content-between")
            # print(course_name)
            if course_name is not None:
                cn = course_name.a.text.strip()
                if ':' in cn:
                    each_course_details['CN'] = course_name.a.text.split(':')[1].strip()
                else:
                    each_course_details['CN'] = course_name.a.text.strip()
            else:
                each_course_details['CN'] = "--------"
                
                
            course_fees = course_card.find('div', class_="jsx-3128659336 text-end ml-4 white-space-nowrap")
            if course_fees is not None:
                each_course_details['CF'] = course_fees.find('span', class_="jsx-3128659336 fs-18 font-weight-semi text-primary-green ml-1").text.strip()
            else:
                each_course_details['CF'] = "::::::::::::"
                
                
            # # 2nd row--
            course_time = course_card.find('span', class_="jsx-3128659336 position-relative")
            if course_time is not None:
                each_course_details['CT'] = course_time.text.strip()
            else:
                each_course_details['CT'] = "|||||||||||"
            
            
            course_type = course_card.find('span', class_="jsx-3128659336 course-separater pl-3 ml-2 position-relative")
            if course_type is not None:
                each_course_details['CType'] = course_type.text.strip()
            else:
                each_course_details['CType'] = "@@@@@@@@@"

                
            print(each_course_details)
                        
except Exception as e:
    print(e)



# -------------------Main Function------------
# getInstituteDetails("https://collegedunia.com/institute/3716-ardent-computech-pvt-ltd-kolkata")
# getInstituteDetails("https://collegedunia.com/institute/3148-the-chennai-school-of-banking-and-management-chennai")