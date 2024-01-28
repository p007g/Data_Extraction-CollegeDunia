import timeit
import pandas as pd
import numpy as np
from courses_wide import Abroad

# start timer
start_time = timeit.default_timer()


courses = ['business', 'engineering', 'sciences', 'social-studies', 'arts',
               'medicine', 'biology', 'accounting', 'psychology', 'finance',
               'economics', 'humanities', 'language', 'education', 'mathematics',
               'history', 'environmental-studies', 'chemistry', 'journalism', 'law', 
               'physics', 'biotechnology', 'nursing', 'design', 'data-science-and-analytics', 
               'information-studies', 'architecture', 'geography', 'graphic-design', 'tourism-and-hospitality', 
               'pharmacy', 'management', 'agriculture', 'fashion-design', 'commerce', 'aviation', 'social-work']

try:
    
    data_frames = {}

    for course in courses:
        
        # make an object------
        data = Abroad(course)

        # access the method-------
        data.city()
        
        info = {
            "Country":data.university_country,
            "Universities Names":data.university_name,
            "University Place":data.university_place,
            "Tuition Fess":data.tuition_fees,
            "Living Fees":data.living_fees
            }
        
        df = pd.DataFrame.from_dict(info, orient='index')
        df = df.transpose()
        df.index = np.arange(1, len(df) + 1)
        df["Rank"] = np.arange(1, len(df) + 1)

        data_frames[course] = df


    excel_file = 'extracted_files\courses-wide-update All Universities Data.xlsx'
        
    # Write each DataFrame to a different sheet in the same Excel file
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:

        for key, data_frame in data_frames.items():

            data_frame.to_excel(writer, sheet_name=key, index=False)


except Exception as e:
    print(e)


# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")