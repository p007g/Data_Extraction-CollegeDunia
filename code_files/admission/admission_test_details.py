import bs
    

#inside link
def getAdmissionDetails(c_link):
    
    soup = bs.Soup(c_link)
    
    
# College Upper---
   
    # college title--------
    clg_place = soup.find('span', class_="jsx-3535035722 text-white fs-14 text-capitalize font-weight-normal mr-2")
    if clg_place is not None:
        print(clg_place.text.strip())
    
    # college affiliation
    aff = soup.find('a', class_="jsx-3535035722 d-flex text-white fs-14 text-capitalize font-weight-normal mr-2 pl-2 clg-detail-separater position-relative")
    if aff is not None:
        print(aff.text.strip())
    
    
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
                
        print(details)
    
    
    
# -------------------Main Function------------
# getAdmissionDetails("https://collegedunia.com/college/13909-kesocietys-rajarambapu-institute-of-technology-rajaramnagar-sangli/admission")
# getAdmissionDetails("https://collegedunia.com/university/59333-uttar-pradesh-university-of-medical-sciences-upums-etawah/admission")
