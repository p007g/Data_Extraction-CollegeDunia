import beautiful_soup

try:
    
    #inside link
    def getInstituteDetails(c_link):
        
        soup = beautiful_soup.Soup(c_link)
        
        
        # institute title--------
        institute_name = soup.find('h1', class_="jsx-3706751501 text-white font-weight-bolder mt-0 mb-1 text-lg").text
        print(institute_name)
        
        
        # institute logo--------
        logo = soup.find('a', class_="jsx-3706751501 college-logo bg-white p-1")
        if logo is not None:
            url = logo.find('img').get('data-src')
            print(url)

            
            
        # institute location--
        loc = soup.find('div', class_="jsx-3706751501 extra-info").find('span', class_="jsx-3706751501 text-white text-uppercase font-weight-bold text-sm mr-3")
        if loc is not None:
            print(loc.text.strip())
            
            
        # Rating----------
        rating = soup.find('span', class_="jsx-3706751501 rating-val font-weight-bolder d-inline-block")
        if rating is not None:
            print(float(rating.text.split('/')[0]))
            
            
            
        # Institute details------
        content = soup.find('div', class_="jsx-1484856324 jsx-1400000905 article-body content-side college-content-section")
        
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
                
                tab = {'Institute Type': '', "Official Website": '', "Email": ''}
                
                for i in range(0, len(info)):
                    
                    cond = info[i].find_all('td')[0].text
                    stat = info[i].find_all('td')[1].text.strip()
                    
                    if cond == 'Institute Type':
                        tab['Institute Type'] = stat
                        
                    elif cond == 'Official Website':
                        tab['Official Website'] = stat
                        
                    elif cond == 'Email':
                        tab['Email'] = stat
                
                print(tab)
        
        else:
            print("No Info") 
    
    # COurses----
        
        course_cards = soup.find('div', class_="jsx-1280987842 courses").find_all('div', class_="jsx-1096428961 program-card mt-4 bg-white")
        
        for course_card in course_cards:
            each_course_details = {}
            
            # 1st row--
            course_name = course_card.find('h3', class_="jsx-1096428961 text-secondary h2 mb-0")
            if course_name is not None:
                each_course_details['CN'] = course_name.a.text.strip()
            else:
                each_course_details['CN'] = "--------"
                
                
            course_fees = course_card.find('div', class_="jsx-1096428961 fees")
            if course_fees is not None:
                each_course_details['CF'] = course_fees.span.text.strip()
            else:
                each_course_details['CF'] = "::::::::::::"
                
                
            # 2nd row--
            course_time = course_card.find('span', class_="jsx-1096428961 year align-items-center font-weight-bold text-sm mr-6")
            if course_time is not None:
                each_course_details['CT'] = course_time.text.strip()
            else:
                each_course_details['CT'] = "|||||||||||"
            
            
            course_type = course_card.find('span', class_="jsx-1096428961 d-block sub-head text-silver")
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
# getfees("https://collegedunia.com/university/25881-iit-madras-indian-institute-of-technology-iitm-chennai")
# getCourses("https://collegedunia.com/college/18041-imt-institute-of-management-technology-ghaziabad")
# getFaculty("https://collegedunia.com/college/18041-imt-institute-of-management-technology-ghaziabad/faculty")