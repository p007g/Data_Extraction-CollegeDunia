import timeit
import pandas as pd
import numpy as np
from code_files.scholarship.scholar import Scholarship

# start Timer
start_time = timeit.default_timer()

try:

    countries = ['canada', 'australia']

    data_frames = {}

    for country in countries:
        # make an object------
        data = Scholarship(country)

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

            data_frames[country] = df
            
        except Exception as e:
            print(e)



    for key, data_frame in data_frames.items():
        print()
        print(f'Country : {key}')
        print(data_frame)
        print()



except Exception as e:
    print(e)

# end Timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")