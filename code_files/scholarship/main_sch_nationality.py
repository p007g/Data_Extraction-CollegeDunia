import timeit
import pandas as pd
import numpy as np
from scholar import Scholarship

# start Timer
start_time = timeit.default_timer()

try:

    countries = ['india', 'canada', 'australia', 'germany', 'hong-kong', 'ireland', 'malaysia', 'netherlands', 
                'new-zealand', 'singapore', 'sweden', 'uk', 'usa', 'france', 'italy', 'uae', 'antigua-and-barbuda', 'switzerland', 'grenada', 'nepal']

    data_frames = {}

    for nationality in countries:
        # make an object------
        data = Scholarship(nationality)

        # access the method-------
        data.city()
        
        try:
            fields = {
                "Scholarship Name":data.scholarship_name,
                "International Student Eligibility":data.scholarship_eligibility, 
                "Amount":data.scholarship_amount,
                "Type of Scholarship":data.scholarship_type,
                "Level of Study":data.scholarship_study_level,
                "No. of Scholarships":data.no_of_scholarships
                }
            
            df = pd.DataFrame.from_dict(fields, orient='index')
            df = df.transpose()
            df.index = np.arange(1, len(df) + 1)
            # df["Rank"] = np.arange(1, len(df) + 1)

            data_frames[nationality] = df
            
        except Exception as e:
            print(e)



    # for key, data_frame in data_frames.items():
    #     print()
    #     print(f'Country : {key}')
    #     print(data_frame)
    #     print()

    excel_file = 'extracted_files/Nationality Wise Scholarship Data.xlsx'
        
    # Write each DataFrame to a different sheet in the same Excel file
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:

        for key, data_frame in data_frames.items():

            data_frame.to_excel(writer, sheet_name=key, index=False)



except Exception as e:
    print(e)

# end Timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")