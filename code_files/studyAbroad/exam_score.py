

def Score(ess):
    scores = ess.find('span', class_="jsx-3255989801 d-flex align-items-center").find_all('span', class_="jsx-3255989801 text-md d-flex align-items-center mr-2")
    
    for score in scores:
        en = score.find('span', class_="jsx-3255989801 text-gray mr-1").text
        es = int(score.find('span', class_="jsx-3255989801 text-primary font-weight-bold").text)