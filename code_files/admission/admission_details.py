import bs
    

clg_location = []
affiliation = []
college_info = []


try:

    #inside link
    def getAdmissionDetails(c_link):
        
        soup = bs.Soup(c_link)
        
        
    # College Upper---
    
        # college place--------
        clg_place = soup.find('span', class_="jsx-3535035722 text-white fs-14 text-capitalize font-weight-normal mr-2")
        if clg_place is not None:
            clg_location.append(clg_place.text.strip())
        else:
           college_info.append("") 
        
        # college affiliation
        aff = soup.find('a', class_="jsx-3535035722 d-flex text-white fs-14 text-capitalize font-weight-normal mr-2 pl-2 clg-detail-separater position-relative")
        if aff is not None:
            affiliation.append(aff.text.strip())
        else:
            affiliation.append("")
        
        
        # details
        clg_details = soup.find('div', class_="cdcms_admission_highlights")
        
        if clg_details is not None:
            # para = clg_details.find_all('p')
            
            details = ""
            for tag in clg_details:
                if tag.name == 'ul':
                    break
                
                if tag.name == 'p':
                    details = details + tag.text
                    
            college_info.append(details)
            
        else:
            college_info.append("")
            
            
except Exception as e:
    print(e)